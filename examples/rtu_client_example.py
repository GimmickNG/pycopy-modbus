#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Create a Modbus RTU client (master) which requests or sets data on a client
device.

The RTU communication pins can be choosen freely (check MicroPython device/
port specific limitations).
The register definitions of the client as well as its connection settings like
bus address and UART communication speed can be defined by the user.
"""

# import modbus client classes
from umodbus.serial import Serial as ModbusRTUMaster
from examples.common.register_definitions import register_definitions
from examples.common.rtu_client_common import IS_DOCKER_MICROPYTHON
from examples.common.rtu_client_common import rtu_pins, baudrate
from examples.common.rtu_client_common import slave_addr, uart_id, read_timeout, exit
from examples.common.sync_client_tests import run_client_tests

client = ModbusRTUMaster(
    pins=rtu_pins,                  # given as tuple (TX, RX)
    baudrate=baudrate,              # optional, default 9600
    # data_bits=8,                  # optional, default 8
    # stop_bits=1,                  # optional, default 1
    # parity=None,                  # optional, default None
    # ctrl_pin=12,                  # optional, control DE/RE
    uart_id=uart_id,                # optional, default 1, see port specific docs
    read_timeout=read_timeout       # optional, default 120
)

if IS_DOCKER_MICROPYTHON:
    # works only with fake machine UART
    assert client._uart._is_server is False


"""
# alternatively the register definitions can also be loaded from a JSON file
import json

with open('registers/example.json', 'r') as file:
    register_definitions = json.load(file)
"""

print('Requesting and updating data on RTU server at address {} with {} baud'.
      format(slave_addr, baudrate))
print()

run_client_tests(client=client,
                 slave_addr=slave_addr,
                 register_definitions=register_definitions)

exit()
