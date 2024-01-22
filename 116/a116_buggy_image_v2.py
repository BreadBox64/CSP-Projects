#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

painter.pensize(40) # Spider Body
painter.circle(20)

legs = 6 # Setup Spider Leg Vars
length = 70
angle = 380 / legs
painter.pensize(5)

for i in range(legs): # Draw Legs
  painter.goto(0,0)
  painter.setheading(angle*i)
  painter.forward(length)
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()