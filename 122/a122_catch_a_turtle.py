# a121_catch_a_turtle.py
#-----import statements-----
from turtle import *
import turtle as turtle
import random
import leaderboard

#-----game configuration----
turtleSize = 2
turtleColor = "#000000"
turtleShape = "circle"

leaderboardFile = "leaderboard.txt"
lb = leaderboard.Leaderboard(leaderboardFile)

score = 0
timer = 30
maxTime = 30
highscore = 0
playerName = ""
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

lbTurtle = turtle.Turtle()
lbTurtle.ht()
lbTurtle.pu()

#-----game functions--------

# manages the leaderboard for top 5 scorers
def manageLeaderboard():
	highScorer = lb.updateLeaderboard(playerName, score)
	lb.drawLeaderboard(highScorer, lbTurtle, score)

def settings():
	mode = tScreen.numinput("A121 - Settings", "Select which setting you would like to change.\n[0 - Time, 1 - Background Color, 2 - Target Color]")
	print(mode)
	if mode == 0:
		response = int(tScreen.numinput("A121 - Settings", "Please enter the timing period in seconds."))
		print(response)
		globals()['maxTime'] = response
	elif mode == 1:
		prompt = "Enter target color as a color string."
		while True:
			response = tScreen.textinput("A121 - Settings", prompt)
			if not (response is None):
				try:
					tScreen.bgcolor(response)
					regenText()
					break
				except turtle.TurtleGraphicsError:
					prompt = "Sorry, that was not a valid color string!\nEnter target color as a valid color string."
	elif mode == 2:
		prompt = "Enter target color as a color string."
		while True:
			response = tScreen.textinput("A121 - Settings", prompt)
			if not (response is None):
				try:
					trtl.color(response)
					writer.color(response)
					regenText()
					break
				except turtle.TurtleGraphicsError:
					prompt = "Sorry, that was not a valid color string!\nEnter target color as a valid color string."
	tScreen.listen()


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
		manageLeaderboard()
		globals()['score'] = 0
	else:
		tScreen.ontimer(onTimerDecrement, 1000)
	regenText()

def turtleClicked(pos, btn):
	if not gameRunning:
		globals()['gameRunning'] = True
		globals()['timer'] = maxTime
		tScreen.ontimer(onTimerDecrement, 1000)
		lbTurtle.clear()
	trtl.goto(random.randint(-size[0], size[0]), random.randint(-size[1], size[1]))
	globals()['score'] += 1
	
	regenText()

#-----events----------------
playerName = tScreen.textinput("A121 - Settings", "What is your username for the leaderboard?")
trtl.onclick(turtleClicked)
tScreen.onkeypress(settings)
tScreen.listen()
regenText()
print(playerName)
tScreen.mainloop()