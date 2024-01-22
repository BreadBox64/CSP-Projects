#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

painter.speed(0)
painter.goto(0, -50) # Spider Body
painter.begin_fill()
painter.circle(50)
painter.end_fill()
painter.goto(0, 30)
painter.begin_fill()
painter.circle(60)
painter.end_fill()

legs = 8 # Setup Spider Leg Vars
legQuarters = int(0.25*legs)
length = 70
angle = 240 / legs
painter.pensize(5)

for j in [1, -1]:
	for i in range(-legQuarters, legQuarters): # Draw Legs
		painter.penup()
		painter.goto(0,0)
		painter.setheading(angle*(i+0.5) - (j*90 - 90))
		painter.forward(50)
		painter.left((j*90 + 90))
		painter.pendown()
		painter.circle(50, -60*j)
  

def eye():
	painter.pendown()
	painter.pensize(5)
	painter.circle(5)
	painter.penup()
painter.fillcolor("#FFFFFF")
painter.pencolor("#FFFFFF")
painter.penup()
painter.goto(12.5, -15) # Spider Body
eye()
painter.goto(-17.5, -15) # Spider Body
eye()

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()