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

DEG90=307
DEG45=int(DEG90/2)
P180=512
P90=P180-DEG90
P270=P180+DEG90
HEAD_FORWARD=int(P180-DEG90/2)
HEAD_MAX=HEAD_FORWARD-10

head = network.get_servo_by_label("head")
head.synchronized = False
head.max_torque = 1023
head.torque_limit = 1023
head.moving_speed = 0
head.goal_position = HEAD_FORWARD
head.torque_enable = 1

larm = network.get_servo_by_label("larm")
larm.synchronized = False
larm.max_torque = 1023
larm.torque_limit = 1023
larm.moving_speed = 0
larm.goal_position = P180
larm.torque_enable = 1

lshoulder = network.get_servo_by_label("lshoulder")
lshoulder.synchronized = False
lshoulder.max_torque = 1023
lshoulder.torque_limit = 1023
lshoulder.moving_speed = 0
lshoulder.goal_position = P180
lshoulder.torque_enable = 1

rarm = network.get_servo_by_label("rarm")
rarm.synchronized = False
rarm.max_torque = 1023
rarm.torque_limit = 1023
rarm.moving_speed = 0
rarm.goal_position = P180
rarm.torque_enable = 1

rshoulder = network.get_servo_by_label("rshoulder")
rshoulder.synchronized = False
rshoulder.max_torque = 1023
rshoulder.torque_limit = 1023
rshoulder.moving_speed = 0
rshoulder.goal_position = P180
rshoulder.torque_enable = 1


import time
while 1:
	e = event.wait()
	if e.type == 7:
		print repr(e)
		if e.axis == 0:
			head.goal_position = int(HEAD_FORWARD - HEAD_MAX * e.value)
			
	elif e.type == 10:
		print "10 %s" % e.button
		if e.button == 7:
			rarm.goal_position = P270
			larm.goal_position = P90 
		elif e.button == 6:
			rarm.goal_position = P90
			larm.goal_position = P270
		elif e.button == 0:
			rarm.goal_position = P270
			larm.goal_position = P90
			rshoulder.goal_position = P270
			lshoulder.goal_position = P90
		elif e.button == 1:
			rarm.goal_position = P270
			larm.goal_position = P90
			rshoulder.goal_position = P90
			lshoulder.goal_position = P270
		elif e.button == 2:
			rarm.goal_position = P90
			larm.goal_position = P270
			rshoulder.goal_position = P270
			lshoulder.goal_position = P90
		elif e.button == 3:
			rarm.goal_position = P90
			larm.goal_position = P270
			rshoulder.goal_position = P90
			lshoulder.goal_position = P270
	elif e.type == 11:
			rarm.goal_position = P180
			larm.goal_position = P180
			rshoulder.goal_position = P180	
			lshoulder.goal_position = P180	
	else:
		print e.type, repr(e)
