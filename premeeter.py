import turtle
from turtle import*
import random
import math
import time
from platform import Platform
from player import *
import tkinter as tk
from functools import partial

turtle.setup(1200,800)
turtle.tracer(0,0)
turtle.hideturtle()
running= True
SLEEP = 0.0077	
turtle.pu()
SCREEN_WIDTH = turtle.getcanvas().winfo_width()//3
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()//3

number_of_platforms= 5
PLATFORMS = []
x_pos = [-350,150,-50,-250,-450]
y_pos = [-500,150,0,-150,-300,-450]
#turtle.register_shape("meetlogo.gif")

'''
def randomize_platform():
	x=random.uniform(width/2-screen_width, screen_width-width/2)
	y=screen_height
'''

for i in range(5):
	x = x_pos[i]
	y = y_pos[i]
	while y == 210:
		y = random.randint(-200,200)
	new_platform = Platform(x,y)
	PLATFORMS.append(new_platform)

def move_platforms_down():
	for new_platforms in PLATFORMS:
		new_platforms.move()


My_Player = Player(0,-340,0.5,0.5)

platform_height= 7
platform_width=3
player_height=50
player_width=125

def collide(platform):
	player_bottom= My_Player.ycor() - player_height
	player_top= My_Player.ycor() + player_height                      
	player_right= My_Player.xcor() + player_width          
	player_left= My_Player.xcor() -player_width


	platform_bottom= platform.ycor()-platform_height
	platform_top= platform.ycor()+platform_height
	platform_right= platfogrm.xcor()+platform_width
	platform_left= platform.xcor()- platform_width

	if platform_top>= player_bottom and platform_bottom<=player_top and platform_right>=player_left and platform_left<=player_right:
		return True
	return False

turtle.update()
global timescore
timescore = 0
timewrite = turtle.Turtle()
timewrite.ht()
turtle.mainloop()