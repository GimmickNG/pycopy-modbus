#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Create a Modbus TCP client (master) which requests or sets data on a client
device.

The TCP port and IP address can be choosen freely. The register definitions of
the client can be defined by the user.
"""

# import modbus client classes
from umodbus.tcp import TCP as ModbusTCPMaster
from examples.common.register_definitions import register_definitions
from examples.common.tcp_client_common import slave_ip, slave_tcp_port, slave_addr, exit
from examples.common.sync_client_tests import run_client_tests

# TCP Master setup
# act as client, get Modbus data via TCP from a client device
# ModbusTCPMaster can make TCP requests to a client device to get/set data
# client = ModbusTCP(
client = ModbusTCPMaster(
    slave_ip=slave_ip,
    slave_port=slave_tcp_port,
    timeout=5)              # optional, default 5

print('Requesting and updating data on TCP server at {}:{}'.
      format(slave_ip, slave_tcp_port))
print()

run_client_tests(client=client,
                 slave_addr=slave_addr,
                 register_definitions=register_definitions)

exit()
