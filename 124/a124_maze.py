import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.screensize(200, 200)
trtl = turtle.Turtle()
trtl.speed(0)

for i in range(10, 400, 10):
	trtl.fd(i)
	trtl.rt(90)

screen.mainloop()