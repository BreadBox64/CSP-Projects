import turtle
import random

screen = turtle.Screen()
screen.setup(600, 600)
screen.delay(0)
screen.screensize(200, 200)
drawTrtl = turtle.Turtle()
drawTrtl.speed(0)
mazeTrtl = turtle.Turtle()
mazeTrtl.speed(0)
mazeTrtl.pu()
mazeTrtl.shape("turtle")
timer = 0
game = False
x = 0
y = 0 #trtl coords dont work

width = 20

def genBarrierPos(doorPos:int, lastDoor:int, len:int) -> int:
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

def setup():
	mazeTrtl.goto(10, -15)
	globals()['x'] = 10
	globals()['y'] = -15
	drawTrtl.st()
	drawTrtl.goto(0, 0)
	drawTrtl.seth(0)
	drawTrtl.clear()
	lastDoors = [0, 0, 0, 0]
	for i in range(width, 440, int(width*0.5)):
		drawTrtl.pd()
		if i > 3*width and i < 400:
			lastDoor = lastDoors.pop(0)
			doorPos = random.randint(0, i-width)
			barrierPos = genBarrierPos(doorPos, lastDoor, i)
			lastDoors.append(doorPos+width)
			# Door
			drawTrtl.fd(doorPos)
			drawTrtl.pu()
			drawTrtl.fd(width)
			drawTrtl.pd()
			drawTrtl.fd(i-(doorPos+width))
			# Barrier
			drawTrtl.pu()
			drawTrtl.bk(i-barrierPos)
			drawTrtl.rt(90)
			drawTrtl.pd()
			drawTrtl.fd(width)
			drawTrtl.pu()
			drawTrtl.bk(width)
			drawTrtl.lt(90)
			drawTrtl.fd(i-barrierPos)
		else:
			drawTrtl.fd(i)
		drawTrtl.rt(90)
	drawTrtl.fd(420)
	drawTrtl.ht()

setup()
screen.listen()
screen.mainloop()