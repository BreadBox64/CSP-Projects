#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl
import random

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  ht.speed(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  vt.speed(0)

  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

def collision(t0, s):
  for t1 in s:
    if (20 > abs(t0.xcor() - t1.xcor())) and (20 > abs(t0.ycor() - t1.ycor())):
      return t1
  return False

lists = [(horiz_turtles, vert_turtles), (vert_turtles, horiz_turtles)]
for step in range(50*2*len(horiz_turtles)):
  for i in lists:
    t = random.choice(i[0])
    t.fd(10)
    collide = collision(t, i[1])
    if collide:
      i[1].remove(collide)
      

wn = trtl.Screen()
wn.mainloop()
