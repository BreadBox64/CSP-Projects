import turtle
import random
import math

test = turtle.Turtle()

for i in range(3):
	test.fd(100)
	test.rt(120)

screen = turtle.Screen()
screen.colormode(255)

color = [200, 100, 100]
indexes = [1, 2, 0]
while True:
	for i in range(3):
		for j in range(100):
			color[i] -= 1
			color[indexes[i]] += 1
			screen.bgcolor(color)


screen.mainloop()