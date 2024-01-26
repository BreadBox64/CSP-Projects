# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random

#-----game configuration----
turtleSize = 2
turtleColor = "#000000"
turtleShape = "circle"

score = 0
timer = 30
gameRunning = False
tScreen = turtle.Screen()

#-----initialize turtle-----
writer = turtle.Turtle()
writer.pu()
writer.ht()
writer.goto(-420, 300)

trtl = turtle.Turtle()
trtl.turtlesize(turtleSize)
trtl.color(turtleColor)
trtl.shape(turtleShape)
trtl.speed(0)
trtl.pu()

#-----game functions--------
def regenText():
	writer.write(f"Score: {str(score)}\nTime Remaining: {timer} secs", font=("Arial", 20, "normal"))

def onTimerDecrement():
	globals()['timer'] -= 1
	if timer == 0:
		globals()['gameRunning'] = False
	else:
		tScreen.ontimer(onTimerDecrement, 1000)
	writer.clear()
	regenText()

def turtleClicked(pos, btn):
	if not gameRunning:
		globals()['gameRunning'] = False
		tScreen.ontimer(onTimerDecrement, 1000)
	trtl.goto(random.randint(-400, 400), random.randint(-300, 300))
	regenText()

#-----events----------------
trtl.onclick(turtleClicked)
regenText()
tScreen.mainloop()