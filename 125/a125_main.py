from turtle import *
from RacingCar import *
from TrackManager import *
import os

screen = Screen()
width, height = (1920, 1080)
halfWidth, halfHeight = (960, 540)
screen.setup(width, height)
screen.tracer(False)
#screen.delay(0)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
trtl = Turtle()
trtl.speed(0)
trtl.color("#5555FF")
trtl.pencolor("#AAAAAA")
trtl.resizemode("user")
trtl.shapesize(2, 2, 2)
trtl.pu()
writer = Turtle()
writer.speed(0)
writer.ht()
writer.pencolor("#FFFFFF")
tm = TrackManager(["02"])
tm.screenRefresh(screen)
rc = RacingCar(Vec2D(-64, 96 - halfHeight), _trackManager = tm)
inputs = {}

def implementKeys(keys):
	def genKF(key:str, val:bool):
		def f():
			keyVal = inputs[key]
			if keyVal != val:
				globals()['inputs'][key] = val
				rc.inputChanged(key, val)
		return f
	kpFunctions = []
	krFunctions = []
	for key in keys:
		cKey = key.capitalize()
		globals()['inputs'][cKey] = False
		kpFunctions.append(genKF(cKey, True))
		krFunctions.append(genKF(cKey, False))
	screen.listen()
	for i,f in enumerate(kpFunctions):
		screen.onkeypress(f, keys[i])
	for i,f in enumerate(krFunctions):
		screen.onkeyrelease(f, keys[i])

def screenUpdate():
	tm.timer += 20
	rc.draw(trtl)
	writer.clear()
	writer.write(f"Time: {'{0:.2f}'.format(tm.timer/1000)}\nG{str(rc.gearing)} [MS: {rc.maxSpeed}, AM {rc.accMult}]\n\n{tm.outputText}", font=("Arial", 24, "bold"))
	screen.update()
	screen.ontimer(screenUpdate, 20)

implementKeys(['w', 'a', 's', 'd', 'q', 'e', 'space'])
screen.listen()
screenUpdate()
screen.mainloop()