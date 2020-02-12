#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")


ARM_PORT = 0
ARM_D = 0
ARM_BACK = 2047
ARM_BOT= 110

CLAW_PORT = 0
CLAW_TICKS = 7000
CLAW_TICKS_BOT = 15000
    
def move_servo_slow(port, current_pos, end_pos,step):
	if end_pos < current_pos:
		step = -step
	for pos in range(current_pos, end_pos, step):
		KIPR.set_servo_position(port, pos)
  		KIPR.msleep(40)
	KIPR.set_servo_position(port,end_pos)
            
            
def arm_bot(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_BOT, step)
        
def arm_down(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_D, step)
        
def arm_back(step):
	move_servo_slow(ARM_PORT, KIPR.get_servo_position(ARM_PORT), ARM_BACK, step)
        
def open_claw(speed):
	KIPR.cmpc(CLAW_PORT)
	KIPR.mav(CLAW_PORT, 1200)
	while KIPR.gmpc(CLAW_PORT) < CLAW_TICKS:
		pass
	KIPR.ao()
  
def close_claw(speed):
	KIPR.cmpc(CLAW_PORT)
	KIPR.mav(CLAW_PORT, -1200)
	while KIPR.gmpc(CLAW_PORT) > -CLAW_TICKS:
		pass
	KIPR.ao()
            
def close_claw_bot(speed):
	KIPR.cmpc(CLAW_PORT)
	KIPR.mav(CLAW_PORT, -2000)
	while KIPR.gmpc(CLAW_PORT) > -CLAW_TICKS_BOT:
		pass
	KIPR.ao()
        
        
        
        
        
        
        
