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
maxTime = 30
highscore = 0
gameRunning = False
tScreen = turtle.Screen()
tScreen.delay(0)

#-----initialize turtle-----
writer = turtle.Turtle()
writer.pu()
writer.ht()
size = tScreen.screensize()
writer.goto(-1*(size[0]), size[1])

trtl = turtle.Turtle()
trtl.turtlesize(turtleSize)
trtl.color(turtleColor)
trtl.shape(turtleShape)
trtl.speed(0)
trtl.pu()

#-----game functions--------
def settings():
	mode = tScreen.numinput("A121 - Settings", "Select which setting you would like to change.\n[0 - Time, 1 - Background Color, 2 - Target Color]")
	print(mode)
	if mode == 0:
		response = tScreen.numinput("A121 - Settings", "Please enter the timing period in seconds.")
		print(response)
		globals()['maxTime'] = response
	elif mode == 1:
		response = tScreen.textinput("A121 - Settings", "Enter background color as a color string.")
		tScreen.bgcolor(response)
	elif mode == 2:
		response = tScreen.textinput("A121 - Settings", "Enter target color as a color string.")
		trtl.color(response)


def regenText():
	text = f"Click the target to start!\nHighscore: {highscore} points\nPress any key to open settings"
	if gameRunning:
		text = f"Score: {str(score)}\nTime Remaining: {round(timer)} secs"
	writer.clear()
	writer.write(text, font=("Arial", 14, "normal"))

def onTimerDecrement():
	globals()['timer'] -= 1
	if timer <= 0:
		globals()['gameRunning'] = False
		if score > highscore:
			globals()['highscore'] = score
		globals()['score'] = 0
	else:
		tScreen.ontimer(onTimerDecrement, 1000)
	regenText()

def turtleClicked(pos, btn):
	if not gameRunning:
		globals()['gameRunning'] = True
		globals()['timer'] = maxTime
		tScreen.ontimer(onTimerDecrement, 1000)
	trtl.goto(random.randint(-size[0], size[0]), random.randint(-size[1], size[1]))
	globals()['score'] += 1
	regenText()

#-----events----------------
trtl.onclick(turtleClicked)
tScreen.onkeypress(settings)
tScreen.listen()
regenText()
tScreen.mainloop()