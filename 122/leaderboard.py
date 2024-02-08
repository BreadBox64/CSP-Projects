# leaderboard.py
# The leaderboard module to be used in Activity 1.2.2

class Leaderboard:
	fileName = ""
	names = []
	scores = []

	# set the levels of scoring
	bronze_score = 15
	silver_score = 20
	gold_score = 25

	def __init__(self, file) -> None:
		self.fileName = file

		leaderboardFile = open(file, "r")

	# return names in the leaderboard file
	def get_names(self):
		return self.names

	# return scores from the leaderboard file
	def get_scores(self):
		return self.scores

	# update leaderboard by inserting the current player and score to the list at the correct position
	def update_leaderboard(self, playerName, playerScore):
		names = self.names
		scores = self.scores
		
		for i in range(len(names)):
			if scores[i] < playerScore:
				scores[i] = playerScore
				names[i] = playerName
		
		leaderboardFile = open(self.fileName, "w")  # this mode opens the file and erases its contents for a fresh start

		for i in range(len(names)):
			leaderboardFile.write(names[i] + "," + str(scores[i]) + "\n")

		leaderboardFile.close()
		self.names = names
		self.scores = scores

	# draw leaderboard and display a message to player
	def draw_leaderboard(self, highScore, turtle, playerScore):
		
		# clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
		font_setup = ("Arial", 20, "normal")
		turtle.clear()
		turtle.penup()
		turtle.goto(-160,100)
		turtle.hideturtle()
		turtle.down()

		# loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
		for index in range(len(self.names)):
			turtle.write(str(index + 1) + "\t" + self.names[index] + "\t" + str(self.scores[index]), font=font_setup)
			turtle.penup()
			turtle.goto(-160,int(turtle.ycor())-50)
			turtle.down()
		
		# move turtle to a new line
		turtle.penup()
		turtle.goto(-160,int(turtle.ycor())-50)
		turtle.pendown()

		# TODO 14: display message about player making/not making leaderboard
		'''
			turtle.write("Congratulations!\nYou made the leaderboard!", font=font_setup)
			turtle.write("Sorry!\nYou didn't make the leaderboard.\nMaybe next time!", font=font_setup)
		'''

		# move turtle to a new line
		turtle.penup()
		turtle.goto(-160,int(turtle.ycor())-50)
		turtle.pendown()
		
		# TODO 15: Display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
		'''
			turtle.write("You earned a gold medal!", font=font_setup)
			turtle.write("You earned a silver medal!", font=font_setup)
			turtle.write("You earned a bronze medal!", font=font_setup)
		'''