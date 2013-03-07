#!/usr/bin/python

from servo.config import ServoConfig
from servo.network import ServoNetwork

config  = ServoConfig()
network = ServoNetwork(config)

import dynamixel, time

tilt = dynamixel.Dynamixel(1, network.net)
tilt.torque_enable = False 
tilt.synchronized=False
tilt.moving_speed = 0
tilt.torque_limit = 800
tilt.max_torque = 800

pan = dynamixel.Dynamixel(19, network.net)
pan.moving_speed = 0
pan.torque_enable = False
pan.synchronized=False
pan.torque_limit = 800
pan.max_torque = 800

arm = dynamixel.Dynamixel(18, network.net)
arm.moving_speed = 0
arm.torque_enable = False
arm.synchronized = False

hand = dynamixel.Dynamixel(3, network.net)
hand.moving_speed = 0
hand.torque_enable = True
hand.synchronized = False

import sys
tilt.goal_position = 846 # 1
hand.goal_position = 279 # 3
arm.goal_position = 210 # 18
pan.goal_position = 211 # 19
time.sleep(2)

tilt.goal_position = 442
hand.goal_position = 557
arm.goal_position = 629
pan.goal_position = 211 
sys.exit(0)

count = 1
while count:
	count -= 1
	print "loop"
	while abs(tilt.current_position - 155) > 3:
		tilt.goal_position = 155
		pan.goal_position = 0
		print pan.current_position
		time.sleep(0.1)
	while abs(tilt.current_position - 855) > 3:
		tilt.goal_position = 855
		pan.goal_position = 1023
		print pan.current_position
		time.sleep(0.1)
