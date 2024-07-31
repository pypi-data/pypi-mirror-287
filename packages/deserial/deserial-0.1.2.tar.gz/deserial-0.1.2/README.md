# deserial

A tool that connects to a serial port and executes scenarios - sends specified commands, and checks the responses.

## Scenario example

For every step, only `input` is required. If `output` is not specified, the step is considered successful if the response is received within `response_timeout_sec` seconds.

```yaml
baudrate: 115200
device: /dev/ttyUSB0
serial_timeout_sec: 5
steps:
- input: AT
  output:
  - OK
- input: ATI
  output:
  - LENA-R8001M10-00C-00
  - ''
  - OK
  post_delay_sec: 1   # before executing the command, wait this long
  pre_delay_sec: 2    # after executing the command, wait this long
  response_timeout_sec: 10  # waiting for the response this long
- input: AT+COPS?
  output:
  - '+COPS: .*'  # every line here is a regex
  - ''
  - OK
  fail_ok: true  # if step fails, it is considered successful
```
