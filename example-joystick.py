#!/usr/bin/python
from pygame import joystick, init, display, event
import os, sys

print "init pygame"
os.environ["SDL_VIDEODRIVER"] = "dummy"
init()
display.init()
display.set_mode((1,1))
joystick.init()

if joystick.get_count() < 1:
  print "please plug a joystick"
  sys.exit(1)

j = joystick.Joystick(0)
j.init()
print "ok"

from servo.config import ServoConfig
from servo.network import ServoNetwork

config  = ServoConfig()
network = ServoNetwork(config)

arm = network.get_servo_by_label("arm")
arm.synchronized = False
arm.max_torque = 1023
arm.torque_limit = 1023
arm.moving_speed = 0
arm.goal_position = 512
arm.torque_enable = 1
arm_goal_position = 512

hand = network.get_servo_by_label("hand")
hand.synchronized = False
hand.max_torque = 1023
hand.torque_limit = 1023
hand.moving_speed = 0
hand.goal_position = 512
hand.torque_enable = 1
hand_goal_position = 512

finger = network.get_servo_by_label("finger")
finger.synchronized = False
finger.cw_angle_limit = 244
finger.ccw_angle_limit = 583
finger.max_torque = 180
finger.torque_limit = 180
finger.moving_speed = 0
FINGER_OPEN = 583
FINGER_CLOSED = 244
finger.goal_position = FINGER_OPEN
finger.torque_enable=1

tilt = network.get_servo_by_label("tilt")
tilt.synchronized = False
tilt.cw_angle_limit = 350
tilt.ccw_angle_limit = 850
tilt.max_torque = 800
tilt.torque_limit = 800
tilt.goal_position = 512
tilt.torque_enable= 1
tilt.goal_position = 400
tilt.moving_speed = 128

tilt_last_update = 0

pan = network.get_servo_by_label("pan")
pan.synchronized = False
pan.cw_angle_limit = 350
pan.ccw_angle_limit = 850
pan.max_torque = 800
pan.torque_limit = 800
pan.goal_position = 512
pan.torque_enable= 1
pan.goal_position = 400
pan.moving_speed = 128

pan_last_update = 0


import time
tilt_goal_position = 512.0
pan_goal_position = 512.0
while 1:
	e = event.wait()
	if e.type == 7:
		if e.axis == 1:
			if time.time() - tilt_last_update > 0.05:
				tilt_last_update = time.time()
				tilt_goal_position -= e.value * 20
				tilt.goal_position = int(tilt_goal_position)	
		if e.axis == 0:
			if time.time() - pan_last_update > 0.05:
				pan_last_update = time.time()
				pan_goal_position += e.value * 20
				pan.goal_position = int(pan_goal_position)
	if e.type == 10:
		if e.button == 7:
			finger.goal_position = FINGER_CLOSED
		if e.button == 0:
			arm_goal_position += 10
			arm.goal_position = arm_goal_position
		if e.button == 1:
			arm_goal_position -= 10
			arm.goal_position = arm_goal_position
		if e.button == 3:
			hand_goal_position += 10
			hand.goal_position = hand_goal_position
		if e.button == 4:
			hand_goal_position -= 10
			hand.goal_position = hand_goal_position
		if e.button == 2:
			finger.max_torque += 50
			finger.torque_limit += 50
		if e.button == 5:
			finger.max_torque -= 50
			finger.torque_limit -= 50
		print finger.max_torque
		print finger.torque_limit
	if e.type == 11:
		if e.button == 7:
			finger.goal_position = FINGER_OPEN
