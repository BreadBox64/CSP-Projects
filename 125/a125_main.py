from turtle import *
from RacingCar import *
#import TrackManager

screen = Screen()
screen.delay(0)
trtl = Turtle()
trtl.speed(0)
trtl.pu()
rc = RacingCar()
inputs = {
	'W': False,
	'A': False,
	'S': False,
	'D': False
}
echos = []
for col in range(175, 239, 16):
	c = '%X' % col
	t = Turtle()
	t.pu()
	t.color(f"#{c}{c}{c}")
	echos.append(t)

def genKF(key:str, val:bool):
	def f():
		keyVal = inputs[key]
		if keyVal == val:
			#print("r")
			pass
		else:
			#print(f"KF - {key} - {val}")
			globals()['inputs'][key] = val
			rc.inputChanged(key, val)
	return f
kpFunctions = []
krFunctions = []
keys = ['w', 'a', 's', 'd']
for key in keys:
	kpFunctions.append(genKF(key.capitalize(), True))
	krFunctions.append(genKF(key.capitalize(), False))
for i,f in enumerate(kpFunctions):
	screen.onkeypress(f, keys[i])
for i,f in enumerate(krFunctions):
	screen.onkeyrelease(f, keys[i])

def screenUpdate():
	rc.draw(trtl, echos)
	screen.ontimer(screenUpdate, 20)

screen.listen()
screenUpdate()
screen.mainloop()