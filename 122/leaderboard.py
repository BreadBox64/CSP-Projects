# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2
import turtle
import os

class Leaderboard:
	fileName = ""
	filePath = ""
	names = []
	scores = []

	# set the levels of scoring
	bronzeScore = 15
	silverScore = 20
	goldScore = 25

	def loadFileData(self) -> None:
		print(self.fileName)
		os.chdir(self.filePath)
		leaderboardFile = open(self.fileName, "r")
		self.names = []
		self.scores = []
		for line in leaderboardFile:
			name,score = line.rstrip().split(',')
			self.names.append(name)
			self.scores.append(int(score))
		leaderboardFile.close()
		
	def __init__(self, file:str, path:str) -> None:
		self.fileName = file
		self.filePath = path
		self.loadFileData()

	# return names in the leaderboard file
	def getNames(self) -> None:
		return self.names.copy()

	# return scores from the leaderboard file
	def getScores(self) -> None:
		return self.scores.copy()

	# update leaderboard by inserting the current player and score to the list at the correct position
	def updateLeaderboard(self, playerName:str, playerScore:int) -> bool:
		names = self.names
		scores = self.scores
		highScorer = False
		
		if len(names) < 5:
			for i in range(len(names)):
				if scores[i] < playerScore:
					scores.insert(i, playerScore)
					names.insert(i, playerName)
					highScorer = True
					break
			if not highScorer:
				scores.append(playerScore)
				names.append(playerName)
				highScorer = True
		else: 
			for i in range(len(names)):
				if scores[i] < playerScore:
					scores.insert(i, playerScore)
					names.insert(i, playerName)
					scores.pop()
					names.pop()
					highScorer = True
					break
		
		if highScorer:
			os.chdir(self.filePath)
			leaderboardFile = open(self.fileName, "w")  # this mode opens the file and erases its contents for a fresh start

			for i in range(len(names)):
				leaderboardFile.write(names[i] + "," + str(scores[i]) + "\n")

			leaderboardFile.close()
			self.names = names
			self.scores = scores
		return highScorer

	def displayMedal(self, turtle:turtle.Turtle, medal:str, fontSetup:tuple) -> None:
		turtle.penup()
		turtle.goto(-160,int(turtle.ycor())-50)
		turtle.pendown()
		turtle.write(f"You earned a {medal} medal!", font=fontSetup)

	# draw leaderboard and display a message to player
	def drawLeaderboard(self, highScore:bool, turtle:turtle.Turtle, playerScore:int) -> None:
		# clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
		fontSetup = ("Arial", 14, "normal")
		turtle.clear()
		turtle.penup()
		turtle.goto(-160,100)
		turtle.hideturtle()
		turtle.down()

		# loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
		for index in range(len(self.names)):
			turtle.write(str(index + 1) + "\t" + self.names[index] + "\t" + str(self.scores[index]), font=fontSetup)
			turtle.penup()
			turtle.goto(-160,int(turtle.ycor())-50)
			turtle.down()
		
		# move turtle to a new line
		turtle.penup()
		turtle.goto(-160,int(turtle.ycor())-50)
		turtle.pendown()

		# TODO 14: display message about player making/not making leaderboard
		if highScore:
			turtle.write("Congratulations!\nYou made the leaderboard!", font=fontSetup)
		else:
			turtle.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=fontSetup)
		
		# TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
		if playerScore >= self.goldScore:
			self.displayMedal(turtle, 'gold', fontSetup)
		elif playerScore >= self.silverScore:
			self.displayMedal(turtle, 'silver', fontSetup)
		elif playerScore >= self.bronzeScore:
			self.displayMedal(turtle, 'bronze', fontSetup)