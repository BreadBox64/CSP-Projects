#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

painter.speed(10)
painter.goto(0, -20) # Spider Body
painter.pensize(40)
painter.circle(20)

legs = 8 # Setup Spider Leg Vars
legQuarters = int(0.25*legs)
length = 70
angle = 240 / legs
painter.pensize(5)

for i in range(-legQuarters, legQuarters): # Draw Legs
  painter.goto(0,0)
  painter.setheading(angle*(i+0.5))
  painter.forward(length)
  painter.right(180)
  painter.forward(2*length)

def eye():
	painter.pendown()
	painter.pensize(10)
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