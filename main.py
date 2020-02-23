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
	arm_bot(50) #joe
	drive_backwards(250, 845)
	close_claw_bot(1160) #grabthatbotty
	drive_straight(250, 400)
	spin_right(100, 80)
	open_claw(1000) #dropit
	for x in range(5):
		spin_left(50,5)
		spin_right(50,5)
            
	arm_down(25) #allhailthegreatyarlie
	spin_left(100,285)
	drive_straight(250,172)
	spin_right(100, 49)
	drive_backwards(250,292) #throwitback and maybe more 
	spin_left(100, 93)
	drive_backwards(250, 518)
	KIPR.msleep(30000) #stop
	drive_straight(250, 525) #missonboll
	spin_left(100, 95)
	arm_ball(9) 
	drive_straight(150,83)
	close_claw_ball(956) #gropetheboll
	arm_ball_up(25)
	drive_backwards (250, 400) 
	spin_left(100, 90) #todemountain
	drive_backwards (250, 80) 
	spin_right (100, 80) #ballyeet
	spin_left(100, 45)
	drive_backwards (250, 75) #originally110 but too far
	open_claw_ball(1000) #ballenlightenment on the mountaintop 
	KIPR.disable_servos()
	
            
	KIPR.create_disconnect()
        
        
        
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
