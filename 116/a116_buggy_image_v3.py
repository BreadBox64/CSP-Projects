#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name painter is used
painter = trtl.Turtle()

painter.goto(0, -20) # Spider Body
painter.pensize(40)
painter.circle(20)

legs = 8 # Setup Spider Leg Vars
length = 70
angle = 240 / legs
painter.pensize(5)

for i in range(legs): # Draw Legs
  painter.goto(0,0)
  painter.setheading(angle*(i))
  painter.forward(length)
painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()