import turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)
screen.screensize(200, 200)
trtl = turtle.Turtle()
trtl.speed(0)

width = 20
lastDoors = [0, 0, 0, 0]

def genBarrierPos(doorPos, lastDoor, len) -> int:
	posList:list = list(range(width, len-width))
	for i in range(doorPos, doorPos+width):
		try:
			posList.remove(i)
		except ValueError:
			pass
	for i in range(lastDoor, lastDoor+width):
		try:
			posList.remove(i)
		except ValueError:
			pass
	return random.choice(posList)

for i in range(width, 400, int(width*0.5)):
	trtl.pd()
	if i > 3*width:
		lastDoor = lastDoors.pop(0)
		doorPos = random.randint(0, i-width)
		barrierPos = genBarrierPos(doorPos, lastDoor, i)
		lastDoors.append(doorPos+width)
		# Door
		trtl.fd(doorPos)
		trtl.pu()
		trtl.fd(width)
		trtl.pd()
		trtl.fd(i-(doorPos+width))
		# Barrier
		trtl.pu()
		trtl.bk(i-barrierPos)
		trtl.rt(90)
		trtl.pd()
		trtl.fd(width)
		trtl.pu()
		trtl.bk(width)
		trtl.lt(90)
		trtl.fd(i-barrierPos)
	else:
		trtl.fd(i)
	trtl.rt(90)

screen.mainloop()