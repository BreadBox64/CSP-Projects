from turtle import *
from RacingCar import *
from TrackManager import *
import os
#import TrackManager

screen = Screen()
screen.delay(0)
os.chdir(os.path.dirname(os.path.realpath(__file__)))
screen.setup(1920, 1080)
screen.bgpic("track01.png")
trtl = Turtle()
trtl.speed(0)
trtl.color("blue")
trtl.pu()
tm = TrackManager(["track01small.png"])
rc = RacingCar(_trackManager = tm)
inputs = {
	'W': False,
	'A': False,
	'S': False,
	'D': False,
	'Q': False,
	'E': False,
	'Space': False,
}

def genKF(key:str, val:bool):
	def f():
		keyVal = inputs[key]
		if keyVal != val:
			globals()['inputs'][key] = val
			rc.inputChanged(key, val)
	return f
kpFunctions = []
krFunctions = []
keys = ['w', 'a', 's', 'd', 'q', 'e', 'space']
for key in keys:
	kpFunctions.append(genKF(key.capitalize(), True))
	krFunctions.append(genKF(key.capitalize(), False))
for i,f in enumerate(kpFunctions):
	screen.onkeypress(f, keys[i])
for i,f in enumerate(krFunctions):
	screen.onkeyrelease(f, keys[i])

def screenUpdate():
	rc.draw(trtl)
	screen.ontimer(screenUpdate, 20)

screen.listen()
screenUpdate()
screen.mainloop()