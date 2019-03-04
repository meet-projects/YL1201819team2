import turtle
from turtle import*
import random
import math
import time
from platform import Platform
from player import *
import tkinter as tk

turtle.setup(900,800)
turtle.tracer(100,1)
turtle.hideturtle()
running= True
sleep = 0.0077	
turtle.pu()
screen_width = turtle.getcanvas().winfo_width()//2
screen_height = turtle.getcanvas().winfo_height()//2



turtle.register_shape("galaxy.gif")
turtle.register_shape("clouds(1).gif")
turtle.register_shape("abed.gif")
turtle.register_shape("ahmad.gif")
turtle.register_shape("kidjumping(1).gif")
turtle.register_shape("gal.gif")
turtle.register_shape("sadek.gif")
turtle.register_shape("background(1).gif")
turtle.register_shape("uriel.gif")
turtle.register_shape("mahed.gif")
 
turtle.bgpic("background(1).gif")
number_of_platforms= 5
platforms= []

plat_width= 125
plat_height=35
plat_dy=.1
x_pos = [-350,150,-50,-250,-450]
global score
score=0
 


def win_game():
	turtle.clear()
	turtle.write("this is Ahmad")
	turtle.Screen().bgpic("ahmad.gif")
	turtle.Screen().bgpic("ahmad.gif")
	# turtle.shape("ahmad.gif")
	#turtle.goto()
	turtle.onkey(win_game2, "space")
def win_game2():
	turtle.clear()
	turtle.write("this is Abed")
	turtle.Screen().bgpic("abed.gif")
	# turtle.shape("abed.gif")
	#turtle.goto()
	turtle.onkey(win_game3, "space")
def win_game3():
	turtle.clear()
	turtle.write("this is Sadek")
	turtle.Screen().bgpic("sadek.gif")
	# turtle.shape("sadek.gif")
	#turtle.goto()
	turtle.onkey(win_game4, "space")
def win_game4():
	turtle.clear()
	turtle.write("this is uriel")
	turtle.Screen().bgpic("uriel.gif")
	# turtle.shape("uriel.gif")
	#turtle.goto()
	turtle.onkey(win_game5, "space")

def win_game5():
	turtle.clear()
	turtle.write("this is gal")
	turtle.Screen().bgpic("gal.gif")
	# turtle.shape("gal.gif")
	#turtle.goto()
	turtle.onkey(win_game6, "space")

def win_game6():
	turtle.clear()
	turtle.write("See you in summer for your first camp!")
	time.sleep(5)
	turtle.quit()


def randomize_platform(platform):
	y=screen_height
	x= random.randint(-screen_width+platform.width, screen_width+platform.width)
	platform.goto(x,y)


def collide(platform):
	player_bottom= player.ycor() - player.height
	player_top= player.ycor() + player.height                      
	player_right= player.xcor() + player.width          
	player_left= player.xcor() -player.width


	platform_bottom= platform.ycor()-platform.height
	platform_top= platform.ycor()+platform.height
	platform_right= platform.xcor()+platform.width
	platform_left= platform.xcor()- platform.width

	if platform_top>= player_bottom and platform_bottom<=player_top and platform_right>=player_left and platform_left<=player_right:
		return True
	return False


def moveplayerright():
	player.right()

def moveplayerleft():
	player.left()

def moveplayerup():
	player.up()
	global score
	score += 1

def move_platforms_down():
	for platform in platforms:
		platform.move()
		if platform.ycor() + platform.height < -screen_height:
			randomize_platform(platform)

player= Player(0,0, 20, 0)
onplat=False

turtle.onkeypress(moveplayerleft,"Left")
turtle.onkeypress(moveplayerup, "Up")
turtle.onkeypress(moveplayerright,"Right")
turtle.listen()

def playgame(screen_height, screen_width, running):
	turtle.listen()
	for i in range(number_of_platforms):
		X = random.randint(-screen_width, screen_width)
		Y = random.randint(-screen_height, screen_height)

		new_plat= Platform(X, Y ,plat_width, plat_height, plat_dy)
		platforms.append(new_plat)
	
	turtle.ontimer(move_platforms_down(), 3*1000)
	while running:
		# print("HERE")
		move_platforms_down()
		player.falling_down(screen_width, screen_height)
		# player.move()
		for platform in platforms:
			if collide(platform):
				if player.ycor()> platform.ycor():
					player.dy = platform.dy
				else:
					running=False

		if player.ycor()< -screen_height:
			running=False

		if screen_width!= int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
			screen_width= int(turtle.getcanvas().winfo_width()/2)
			screen_height= int(turtle.getcanvas().winfo_height()/2)

		if score == 10:
			turtle.Screen().bgpic("clouds(1).gif")
		if score == 20:
			turtle.Screen().bgpic("galaxy.gif")
		if score == 30:
			turtle.reset()
			turtle.ht()
			turtle.pu()
			turtle.write("Congratulations!, you are now a Y1 MEET student", font=("Arial", 10, "normal"), align="center")
			# turtle.write("click the "space" bar to continue!", font=("Arial",100,"normal"), align="center")
			#turtle.listen()
			turtle.onkey(win_game, "space")

			
				# turtle.clear()
				# turtle.ht()
				# turtle.write("MEET your coordinators", font=("Arial", 100, "normal"), align="center")
				# turtle.write("click the "space" bar to continue!", font=("Arial",100,"normal"), align=(0,-100)
				# turtle.onkey(win_game, "space")

		turtle.update()

playgame(screen_height, screen_width, running)
