from turtle import *
from RacingCar import *
from TrackManager import *
import os

screen = Screen()
screen.setworldcoordinates(-960, -580, 960, 580)
screen.setup(1920, 1080)
screen.delay(0)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
trtl = Turtle()
trtl.speed(0)
trtl.color("blue")
trtl.pu()
writer = Turtle()
writer.speed(0)
writer.goto(0, 400)
tm = TrackManager(["02"], writer)
tm.screenRefresh(screen)
rc = RacingCar(Vec2D(0, -50), _trackManager = tm)
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
	screen.ontimer(screenUpdate, 20)

implementKeys(['w', 'a', 's', 'd', 'q', 'e', 'space'])
screen.listen()
screenUpdate()
screen.mainloop()