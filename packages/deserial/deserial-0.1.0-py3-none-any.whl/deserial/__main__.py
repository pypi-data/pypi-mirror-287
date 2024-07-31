import argparse
import logging
import re
import sys
import time
from dataclasses import dataclass
from typing import Optional, cast

import coloredlogs
import dataclass_factory
import serial
import yaml


class ScenarioError(Exception):
    def __init__(self, message: str, request: str = "") -> None:
        self.request = request
        super().__init__(message)


@dataclass
class Step:
    input: str
    output: Optional[list[str]]
    response_timeout_sec: int = 10  # seconds
    pre_delay_sec: int = 0  # seconds
    post_delay_sec: int = 0  # seconds
    fail_ok: bool = False


@dataclass
class Scenario:
    device: str
    baudrate: int
    timeout_sec: int = 5  # seconds
    steps: list[Step]

    @staticmethod
    def from_dict(data: dict) -> "Scenario":
        f = dataclass_factory.Factory()
        return cast(Scenario, f.load(data))

    @staticmethod
    def from_yaml(yaml_path: str) -> "Scenario":
        with open(yaml_path) as f:
            return Scenario.from_dict(yaml.safe_load(f))


def serial_request(port: serial.Serial, logger: logging.Logger, request: str, wait_response_sec: int = 5) -> list[str]:
    logger.debug(f"<-- {request}")

    # do write and flush
    port.write(data=f"{port}\r\n".encode("ascii"))
    port.reset_input_buffer()
    if wait_response_sec <= 0:
        logger.debug("--> not expecting response")
        return

    time.sleep(0.2)
    response_data = []
    wait_counter = 0
    command_reply_found = False
    newline_after_command_reply_found = False
    result_after_newline_found = False

    start_time = time.time()

    while (
        port.in_waiting >= 1
        or command_reply_found is False
        or newline_after_command_reply_found is False
        or result_after_newline_found is False
    ):
        if port.in_waiting == 0:
            wait_counter += 1

        if time.time() - start_time > wait_response_sec:
            raise ScenarioError(message=f"Timeout waiting reply ({wait_counter})", request=request)

        time.sleep(0.01)

        try:
            response_line = port.readline().decode("utf-8").rstrip("\r\n")
        except UnicodeDecodeError as e:
            raise ScenarioError(message=f"Received non-utf8 data: {e}", request=request) from e

        if response_line == request:
            command_reply_found = True
        elif command_reply_found is True and response_line == "":
            newline_after_command_reply_found = True
        elif command_reply_found is True and newline_after_command_reply_found is True and len(response_line) > 0:
            result_after_newline_found = True

        if (
            command_reply_found is True
            and newline_after_command_reply_found is True
            and result_after_newline_found is True
        ):
            response_data.append(response_line)

    logger.debug(f"--> {response_data}")
    return response_data


def main() -> None:
    parser = argparse.ArgumentParser(description="DeSerial")
    parser.add_argument("-p", "--port", help="Serial port to use")
    parser.add_argument("-b", "--baud", help="Baud rate to use", type=int)
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")
    parser.add_argument("scenario", help="Scenario to run", type=argparse.FileType("r"))
    args = parser.parse_args()

    if args.debug:
        coloredlogs.install(level=logging.DEBUG)
    else:
        coloredlogs.install(level=logging.INFO)

    scenario = Scenario.from_yaml(args.scenario.name)

    # try to open serial port
    try:
        device = args.port or scenario.device
        baudrate = args.baud or scenario.baudrate

        port = serial.Serial(port=device, baudrate=baudrate, timeout=scenario.timeout_sec)
    except serial.SerialException as e:
        die(f"Failed to open serial port {device} with baudrate {baudrate}, error: {e}")

    logging.info(f"Connected to {device} with baudrate {baudrate}")
    logging.info(f"Running scenario {args.scenario.name}")
    for i, step in enumerate(scenario.steps):
        logger = logging.getLogger(f"step-{i}")
        logger.warning(f"Executing '{step.input}'")
        try:
            if step.pre_delay_sec > 0:
                logger.debug(f"pre-delay {step.pre_delay_sec} seconds")
                time.sleep(step.pre_delay_sec)

            output = serial_request(
                port=port, request=step.input, logger=logger, wait_response_sec=step.response_timeout_sec
            )

            if step.post_delay_sec > 0:
                logger.debug(f"post-delay {step.post_delay_sec} seconds")
                time.sleep(step.post_delay_sec)

            # match output with expected
            if step.output is None:
                logger.info("no output expected")
                continue

            for i, (actual, expected) in enumerate(zip(output, step.output)):
                logger.debug(f"actual: {actual}, expected: {expected}")
                # actual is a string, expected is a regex

                try:
                    R = re.compile(expected)
                except re.error as e:
                    die(f"Output '{expected}' at index {i} is not a valid regex (request={step.input}): {e}")

                if not R.match(actual):
                    raise ScenarioError(
                        message=f"Output '{actual}' at index {i} does not match regex '{expected}'", request=step.input
                    )

            logger.info("output matches")
            continue
        except ScenarioError as e:
            if step.fail_ok:
                logger.info("marked as fail_ok: True, skipping")
                continue
            else:
                die(f"Step {i}/{step.input} failed: {e}")

        except serial.SerialException as e:
            die(f"Port suddenly closed? Error: {e}")
        except Exception as e:
            die(f"Failed to execute step {i}/{step.input}, unexpected error: {e}")

    logging.info("Scenario completed successfully")


if __name__ == "__main__":
    main()


def die(message: str) -> None:
    logging.critical(message)
    sys.exit(1)
