#!/usr/bin/python

from servo.config import ServoConfig
from servo.network import ServoNetwork

config  = ServoConfig()
network = ServoNetwork(config)

head = network.get_servo_by_label("head")
neck  = network.get_servo_by_label("neck")

head.goal_position = 400
neck.goal_position = 400
