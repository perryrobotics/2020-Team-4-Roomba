#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def drive_straight(speed, dist_to_go):
	KIPR.set_create_distance(0)
  	KIPR.create_drive_direct(speed, speed)
  	while KIPR.get_create_distance() < dist_to_go:
		print KIPR.get_create_distance(), ":", dist_to_go
		pass
 	KIPR.create_drive_direct(0,0)
 
def drive_backwards(speed, dist_to_go):
	KIPR.set_create_distance(0)
  	KIPR.create_drive_direct(-speed, -speed)
  	while KIPR.get_create_distance() > -dist_to_go:
		pass
 	KIPR.create_drive_direct(0,0)
            
def spin_left(speed, angle_to_go):
	KIPR.set_create_total_angle(0)
  	KIPR.create_spin_CCW(speed)
  	while KIPR.get_create_total_angle() < angle_to_go:
		pass
 	KIPR.create_drive_direct(0,0)
            
def spin_right(speed, angle_to_go):
	KIPR.set_create_total_angle(0)
  	KIPR.create_spin_CW(speed)
  	while KIPR.get_create_total_angle() > -angle_to_go:
		pass
 	KIPR.create_drive_direct(0,0)
            
def drive_till_bump(speed):
	KIPR.create_drive_direct(speed, speed)
  	while KIPR.get_create_lbump() == 0 and KIPR.get_create_rbump()==0:
		pass
 	KIPR.create_drive_direct(0,0)
        
