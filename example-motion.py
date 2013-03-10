#!/usr/bin/python

from servo.config import ServoConfig
from servo.network import ServoNetwork
from servo.motion import Position

config  = ServoConfig()
network = ServoNetwork(config)

for ident in network.config.ids:
	d = network.get_servo(int(ident))
	d.torque_enable = 1
	d.moving_speed = 1023

walk_0 = Position("walk_0")
walk_1 = Position("walk_1")
walk_2 = Position("walk_2")
walk_3 = Position("walk_3")

import time
while True:
	walk_0(network)
	time.sleep(0.5)
	walk_1(network)
	time.sleep(0.5)
	walk_2(network)
	time.sleep(0.5)
	walk_3(network)
	time.sleep(0.5)
