#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Create an async Modbus TCP client (master) which requests or sets data on a
client device.

The TCP port and IP address can be choosen freely. The register definitions of
the client can be defined by the user.
"""

# system packages
try:
    import uasyncio as asyncio
except ImportError:
    import asyncio

# import modbus client classes
from umodbus.asynchronous.tcp import AsyncTCP as ModbusTCPMaster
from examples.common.register_definitions import register_definitions
from examples.common.tcp_client_common import slave_ip, slave_tcp_port
from examples.common.tcp_client_common import slave_addr, exit
from examples.common.async_client_tests import run_client_tests


async def start_tcp_client(client, port, unit_id, timeout):
    # TCP Master setup
    # act as client, get Modbus data via TCP from a client device
    # ModbusTCPMaster can make TCP requests to a client device to get/set data
    client = ModbusTCPMaster(
        slave_ip=client,
        slave_port=port,
        timeout=timeout)

    # unlike synchronous client, need to call connect() here
    await client.connect()
    if client.is_connected:
        print('Requesting and updating data on TCP client at {}:{}'.
              format(client, port))
        print()

        await run_client_tests(client=client,
                               slave_addr=unit_id,
                               register_definitions=register_definitions)


# create and run task
task = start_tcp_client(client=slave_ip,
                        port=slave_tcp_port,
                        unit_id=slave_addr,
                        timeout=5)
asyncio.run(task)

exit()
