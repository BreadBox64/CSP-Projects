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

wn = trtl.Screen()
wn.setworldcoordinates(-400, -100, 100, 400)

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
  vt.goto(-tloc, 350)
  vt.setheading(270)
  vt.speed(0)

  tloc += 50

oldColors = []

def collision(t0, s0, t1, s1):
  a = (t0.xcor() + s0 + 20) < t1.xcor()
  b = (t0.xcor() - 20) > t1.xcor()
  c = ((t1.ycor() - s1) - 20) > t0.ycor()
  d = (t1.ycor() + 20) < t0.ycor()
  print(f"[{str(a)}, {str(b)}, {str(c)}, {str(d)}]")
  if (a or b) and (c or d):
    t0.fd(s0)
    oldColors.index(t1)
    t1.fd(s1)
  else:
    t0.fd(s0)
    t1.fd(s1)
    oldColors[t1.color()[1]] = t1
    t1.color("grey")
    t1.bk(s1)

for i in range(50):
  for ht in horiz_turtles:
    for vt in vert_turtles:
      collision(ht, 2, vt, 2)    

for i in [horiz_turtles, vert_turtles]:
  for t in i:
    t.color("grey")

wn.mainloop()
