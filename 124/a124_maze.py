import turtle
from random import randint

screen = turtle.Screen()
screen.setup(600, 600)
screen.screensize(200, 200)
trtl = turtle.Turtle()
trtl.speed(0)

width = 20
for i in range(width, 400, int(width*0.5)):
	trtl.pd()
	if i > 3*width:
		doorPos = randint(0, i-width)
		barrierPos = randint(width, i-width)
		barrierPos = barrierPos if barrierPos <= doorPos or barrierPos >= (doorPos+width) else doorPos
		# Door
		trtl.fd(doorPos)
		trtl.pu()
		trtl.fd(width)
		trtl.pd()
		trtl.fd(i-(doorPos+width))
		# Barrier
		trtl.pu()
		trtl.bk(barrierPos)
		trtl.rt(90)
		trtl.pd()
		trtl.fd(width)
		trtl.pu()
		trtl.bk(width)
		trtl.lt(90)
		trtl.fd(barrierPos)
	else:
		trtl.fd(i)
	trtl.rt(90)

screen.mainloop()