import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.screensize(200, 200)
trtl = turtle.Turtle()
trtl.speed(0)

width = 10
for i in range(width, 400, width):
	if i > 3*width:
		trtl.fd(i-(3*width))
		trtl.rt(90)
		trtl.fd(width*2)
		trtl.bk(width*2)
		trtl.lt(90)
		trtl.fd(width)
		trtl.pu()
		trtl.fd(width)
		trtl.pd()
		trtl.fd(width)
	else:
		trtl.fd(i)
	trtl.rt(90)

screen.mainloop()