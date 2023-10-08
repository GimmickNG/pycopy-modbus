#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Create a Modbus TCP server (slave) which can be requested for data or set with
specific values by a client device.

The TCP port and IP address can be choosen freely. The register definitions of
the server can be defined by the user.
"""

# import modbus server classes
from umodbus.tcp import ModbusTCP

# import relevant auxiliary script variables
from examples.common.register_definitions import register_definitions, setup_callbacks
from examples.common.tcp_server_common import local_ip, tcp_port
from examples.common.tcp_server_common import IS_DOCKER_MICROPYTHON

# ModbusTCP can get TCP requests from a client device to provide/set data
server = ModbusTCP()

# alternatively the register definitions can also be loaded from a JSON file
# this is always done if Docker is used for testing purpose in order to keep
# the server registers in sync with the test registers
if IS_DOCKER_MICROPYTHON:
    import json
    with open('registers/example.json', 'r') as file:
        register_definitions = json.load(file)  # noqa: F811

# setup remaining callbacks after creating server
setup_callbacks(server, register_definitions)

# check whether server has been bound to an IP and port
is_bound = server.get_bound_status()
if not is_bound:
    server.bind(local_ip=local_ip, local_port=tcp_port)

print('Setting up registers ...')
# use the defined values of each register type provided by register_definitions
server.setup_registers(registers=register_definitions)
# alternatively use dummy default values (True for bool regs, 999 otherwise)
# server.setup_registers(registers=register_definitions, use_default_vals=True)
print('Register setup done')

print('Serving as TCP server on {}:{}'.format(local_ip, tcp_port))

while True:
    try:
        result = server.process()
    except KeyboardInterrupt:
        print('KeyboardInterrupt, stopping TCP server...')
        break
    except Exception as e:
        print('Exception during execution: {}'.format(e))

print("Finished providing/accepting data as server")
