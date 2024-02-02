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
oldHorizColors = horiz_colors.copy()
oldVertColors = vert_colors.copy()

wn = trtl.Screen()
wn.setworldcoordinates(-400, -1400, 1400, 400)
wn.delay(1)

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

def collision(t0, s0, i0, t1, s1, i1):
  a = (t0.xcor() + s0 + 20) < t1.xcor()
  b = (t0.xcor() - 20) > t1.xcor()
  c = ((t1.ycor() - s1) - 20) > t0.ycor()
  d = (t1.ycor() + 20) < t0.ycor()
  #print(f"[{str(a)}, {str(b)}, {str(c)}, {str(d)}]")
  print(f"{i0}, {i1}")
  if (a or b) or (c or d): # Not colliding on x or not colliding on y
    t0.color(oldHorizColors[i0])
    t0.fd(s0)
    t1.color(oldVertColors[i1])
    t1.fd(s1)
  else:
    if (a or b): # Not colliding on x - therefore, Colliding on y
      t1.fd(s1)
      color = t1.color()[1]
      if color != "grey":
        oldVertColors[i0] = color
      t0.color("grey")
    else: # Colliding on x
      t0.fd(s0)
      color = t1.color()[1]
      if color != "grey":
        oldHorizColors[i1] = color
      t1.color("grey")

for i in range(50):
  h = 0
  for ht in horiz_turtles:
    v = 0
    for vt in vert_turtles:
      dist = 1
      collision(ht, dist, h, vt, dist, v)
      v += 1
    h += 1

for i in [horiz_turtles, vert_turtles]:
  for t in i:
    t.color("grey")

wn.mainloop()
