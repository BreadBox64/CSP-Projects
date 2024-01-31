#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["#FF0000", "#FFAA00", "#AAAA00", "#AAFF00", "#00FF00", "#00FFAA", "#00AAAA", "#00AAFF", "#0000FF", "#AA00FF", "#AA00AA", "#FF00AA"]

tColorLength = len(turtle_colors)
for i in range(tColorLength):
  s = turtle_shapes.pop(0)
  turtle_shapes.append(s)
  t = trtl.Turtle(shape=s)
  t.color(turtle_colors[i])
  t.pu()
  t.speed(10)
  t.pensize(tColorLength-i)
  my_turtles.append(t)

#  Define starting position
startPos = (0, 0)
heading = 0
length = 50

# Move the turtules to draw the figure
for t in my_turtles:
  t.goto(startPos)
  t.pd()
  t.setheading(heading - 45)  
  t.forward(length)
  startPos = t.pos()
  heading = t.heading()
  length += 10

# Advance the position of the turtle
#startx = startx + 50
#starty = starty + 50

wn = trtl.Screen()
wn.mainloop()