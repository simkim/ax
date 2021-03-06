#!/usr/bin/python

from servo.config import ServoConfig
from servo.network import ServoNetwork
from servo.motion import Position

config  = ServoConfig()
network = ServoNetwork(config)

network.apply_all(torque_enable=1, moving_speed=1023)

walk_0 = Position("pos/puppy/walk_0")
walk_1 = Position("pos/puppy/walk_1")
walk_2 = Position("pos/puppy/walk_2")
walk_3 = Position("pos/puppy/walk_3")

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
