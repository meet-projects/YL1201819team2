import turtle
from turtle import*
import random
import math
import time

turtle.register_shape("platform.gif")

class Platform(Turtle):
	def __init__(self, x, y, width, height, dy):
		Turtle.__init__(self)
		self.pu()
		turtle.ht()
		self.goto(x,y)
		self.shape("platform.gif")
		#register shape of the platform and change it
		self.shapesize=60
		self.width= width
		self.height=height
		self.dy=dy

	def move(self):
		old_x = self.xcor()
		old_y = self.ycor() 
		new_y = old_y-self.dy
		self.goto(old_x,new_y)

