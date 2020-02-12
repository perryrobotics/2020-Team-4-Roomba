#!/usr/bin/python
import os, sys
import ctypes
from motion import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():
  	print "Hello World"
 	KIPR.create_connect()    	
	KIPR.enable_servos()
	arm_back(10)
	while KIPR.a_button()==0:
		pass
	print("Starting in 3 seconds!!!")
	KIPR.msleep(3000)
	arm_bot(7)
	#open_claw(1000)
	drive_backwards(250, 845)
	close_claw_bot(1160)
	drive_straight(250, 400)
	spin_right(100, 80)
	open_claw(1000)
	arm_back(10)
	spin_left(100,245)
	
            
	
            
	KIPR.create_disconnect()
        
        
        
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
