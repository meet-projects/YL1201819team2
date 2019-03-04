import turtle
from turtle import*
import random
import math
import time






UP=0
DOWN=1
LEFT=2
RIGHT=3



direction= UP





# func = partial(up, running)
# turtle.onkeypress(up, UP_ARROW) 
# turtle.onkeypress(left,"Left")
# turtle.onkeypress(up, "Up")
# turtle.onkeypress(right,"Right")
# turtle.listen()
turtle.register_shape("kidjumping(1).gif")

class Player(Turtle):
	def __init__(self, x, y, dx, dy):
		Turtle.__init__(self)
		self.pu()
		turtle.ht()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		#self.shape("square")#players shape
		self.shapesize(50/10)
		self.height = 60
		self.width= 40
		self.shape("kidjumping(1).gif")


	def up(self):
		# print("going up")
		direction = UP
		self.goto(self.xcor() , self.ycor() + 250*self.dy)

	def left(self):
		direction = LEFT
		self.goto(self.xcor() - self.dx , self.ycor())


	def right(self):
		direction = RIGHT
		self.goto(self.xcor() + self.dx , self.ycor())

	# def move(self):
	# 	old_x = self.xcor()
	# 	old_y = self.ycor()

	# 	global direction
	# 	if direction==RIGHT:
	# 		self.goto(old_x + self.dx , old_y)
	# 		#print("You moved right!")
	# 	elif direction==LEFT:
	# 		self.goto(old_x - self.dx , old_y)
	# 		#print("You moved left!")
	# 	elif direction==UP :
	# 		self.goto(old_x , old_y + self.dy)
	
	def falling_down(self, screen_width, screen_height):
		old_x = self.xcor()
		old_y = self.ycor()
		new_y = old_y - self.dy
		self.goto(old_x,new_y)

		if self.xcor() > screen_width:
			self.goto(-screen_width, self.ycor())
		if old_x < -screen_width:
			self.goto(-screen_width, self.ycor())
		if new_y <= -screen_height:
			running=False
		self.dy =self.dy + 0.001
		print(self.dy)

'''
pl= Player(0,0, 1, 2)
while True:
	pl.move()
	turtle.listen()
turtle.mainloop()
'''