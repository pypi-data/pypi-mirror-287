import logging
import time

import serial
from deserial.errors import ScenarioError


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
            raise ScenarioError(
                message=f"Timeout waiting reply ({wait_counter}). Reply: '{response_data}'", request=request
            )

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
