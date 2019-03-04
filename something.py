import turtle
from turtle import *
import time
import math
import random

platform_height= 7
platform_width=3
player_height=4
player_width=2

def collide(platform):#
	player_bottom= player.ycor()-player_height
	player_top= player.ycor() +player_height
	player_right= player.xcor()+player_width
	player_left= player.xcor()- player_width


	platform_bottom= platform.ycor()-platform_height
	platform_top= platform.ycor()+platform_height
	platform_right= platform.xcor()+platform_width
	platform_left= platform.xcor()- platform_width

	if platform_top>= player_bottom and platform_bottom<=player_top and platform_right>=player_left and platform_left<=player_right:
		return True
	return False
