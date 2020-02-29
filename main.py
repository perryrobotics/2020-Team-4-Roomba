#!/usr/bin/python
import os, sys
import ctypes
from motion import *
from effectors import *
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def main():

#===============================================================
#				GET INTP START POSITION
#==============================================================

  	print "Hello World"
 	KIPR.create_connect() 
	KIPR.create_full()
	KIPR.enable_servos()
	arm_back(30)
	dump_start(30)
        
	while KIPR.a_button()==0:
		pass
	print("Starting in 3 seconds!!!")
	KIPR.msleep(3000)
#=================GO GET BOTGUY=======================
	arm_bot(50) #joe
	drive_backwards(250, 890)

	close_claw_bot(1160) #grabthatbotty
	drive_straight(150, 400)
	spin_right(100, 80)
	open_claw(1000) #dropit
	"""
	for x in range(5):  #shake 5 times
		spin_left(50,5)
		spin_right(50,5)
	"""
	arm_half(50)
#===================BOT GUY SCORED===================
            
#===================ASTRONAUTS====================
	spin_right(100,115)
	#drive_straight(250,390)
	drive_till_bump(100) # hit pipe by mine carts
	drive_backwards(50,50) #get poff the pipe a little
	spin_right(100,55) #turn towards platform
	drive_backwards(50, 200) # drive towards platform   MAY NEED TO ADJUST!!!   
	spin_left(50,30) #line up with astronauts
	
	back_till_black(50)
	drive_backwards (100, 145) #collect astronaughts
	spin_left(50, 43) #spin them into basket
    
	spin_right(50, 43) #spin back
	drive_straight(50,150)  #get away from pipe
	spin_left(50,45)
	drive_backwards(100,265)
	spin_right(100,37) #turn to face ore boxes
	drive_backwards(150, 130) #into the ore boxes
	spin_left(100, 95) #spin to face start box
	drive_backwards(150,250)
	dump_dump(25)
	drive_backwards(150, 168)
	#KIPR.msleep(10000) #stop
	drive_till_black(100)
	drive_straight(100, 150)
	#drive_straight(150, 500) #missonboll but maybe stop and dump astronauts first 
	spin_left(100, 90)
	arm_ball(9) 
	drive_straight(150,80) #go towards the ball
	close_claw_ball(956) #gropetheboll
	arm_ball_up(25)
	drive_backwards (250, 400) 
	spin_left(100, 90) #todemountain
	drive_backwards (250, 80) 
	spin_right (100, 80) #ballyeet
	spin_left(100, 55)
	drive_backwards (250, 100) #originally110 but too far
	open_claw_ball(1000) #ballenlightenment on the mountaintop 
	KIPR.disable_servos()
	KIPR.create_disconnect()
        
        
        
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
