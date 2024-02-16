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

inputs = {
	'w': False,
	'a': False,
	's': False,
	'd': False,
	'Up': False,
	'Down': False,
	'Left': False,
	'Right': False,
}
# This is copied from my 1.2.5 because this is easier and better than setting it up manually
screen.listen()
def genKF(key:str, val:bool):
	def f():
		keyVal = inputs[key]
		if keyVal != val:
			globals()['inputs'][key] = val
	return f
keys = ['w', 'a', 's', 'd', 'Up', 'Down', 'Left', 'Right']
kpFunctions = []
krFunctions = []
for key in keys:
	kpFunctions.append(genKF(key, True))
	krFunctions.append(genKF(key, False))
for i,f in enumerate(kpFunctions):
	screen.onkeypress(f, keys[i])
for i,f in enumerate(krFunctions):
	screen.onkeyrelease(f, keys[i])

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
		
def getAngle(vector:tuple) -> int:
	match vector:
		case (-1, -1):
			return 225
		case (-1, 0):
			return 180
		case (-1, 1):
			return 135
		case (0, -1):
			return 270
		case (0, 0):
			return mazeTrtl.heading()
		case (0, 1):
			return 90
		case (1, -1):
			return 315
		case (1, 0):
			return 0
		case (1, 1):
			return 45
	return None # Passed an invalid vector

def gameLoop():
	screen.ontimer(gameLoop, 50)
	vertical = int(inputs['w'] or inputs['Up']) - int(inputs['s'] or inputs['Down'])
	horizontal = int(inputs['d'] or inputs['Right']) - int(inputs['a'] or inputs['Left'])
	mazeTrtl.seth(getAngle((horizontal, vertical)))
	mazeTrtl.goto(mazeTrtl.xcor() + 3*horizontal, mazeTrtl.ycor() + 3*vertical)
	globals()['x'] += 3*horizontal
	globals()['y'] += 3*vertical

setup()
game = True
screen.ontimer(gameLoop, 50)
screen.listen()
screen.mainloop()