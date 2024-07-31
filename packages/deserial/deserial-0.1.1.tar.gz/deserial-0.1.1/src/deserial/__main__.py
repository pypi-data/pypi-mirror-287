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
from deserial.errors import ScenarioError
from deserial.util import serial_request


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
    steps: list[Step]
    device: Optional[str] = None
    baudrate: Optional[int] = None
    serial_timeout_sec: int = 5  # seconds

    @staticmethod
    def from_dict(data: dict) -> "Scenario":
        f = dataclass_factory.Factory()
        return cast(Scenario, f.load(data))

    @staticmethod
    def from_yaml(yaml_path: str) -> "Scenario":
        with open(yaml_path) as f:
            return Scenario.from_dict(yaml.safe_load(f))

    def to_dict(self) -> dict:
        f = dataclass_factory.Factory()
        return f.dump(self)

    @staticmethod
    def example() -> str:
        s = Scenario(
            device="/dev/ttyUSB0",
            baudrate=115200,
            serial_timeout_sec=5,
            steps=[
                Step(
                    input="AT",
                    output=["OK"],
                    response_timeout_sec=2,
                ),
                Step(
                    input="ATI",
                    output=["LENA-R8001M10-00C-00", "", "OK"],
                ),
                Step(
                    input="AT+COPS?",
                    output=["+COPS: .*", "", "OK"],
                ),
            ],
        )

        return yaml.dump(s.to_dict())


def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"Tool that connects to a serial port and executes scenarios. Scenario example (example.yaml): \n\n{Scenario.example()}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("scenario", help="Scenario to run", type=argparse.FileType("r"))
    parser.add_argument("-p", "--port", default=None, help="Serial port to use")
    parser.add_argument("-b", "--baud", default=None, type=int, help="Baud rate to use")
    parser.add_argument("-d", "--debug", default=False, action="store_true", help="Enable debug mode")
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
        if not device:
            die("No device specified")
        if not baudrate:
            die("No baudrate specified")

        port = serial.Serial(port=device, baudrate=baudrate, timeout=scenario.serial_timeout_sec)
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
