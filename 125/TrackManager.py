from PIL import Image
from math import floor
from turtle import _Screen,Turtle

frictionCoeffs = { #includes all colors
	(0, 0, 0, 255): 0.5,
	(64, 64, 64, 255): 0.15,
	(128, 128, 128, 255): 0.15,
	(255, 255, 255, 255): 0.15,
	(32, 128, 32, 255): 0.4,
	(128, 0, 0, 255): 0.15,
	(255, 0, 0, 255): 0.15,
}

events = {
	(0, 0, 0, 255): 2,
	(255, 255, 255, 255): 3,
	(255, 0, 0, 255): 1,
}

font = ("Arial", 10, "normal")

class Track:
	img:Image.Image
	pixelValues:list
	width:int
	height:int

	def __init__(self, imagePath:str) -> None:
		img = Image.open(imagePath, 'r')
		self.width, self.height = img.size
		self.img = img
		self.pixelValues = list(img.getdata())

	def getCoeffAtPoint(self, x:int, y:int) -> float:
		color = self.pixelValues[self.width*y+x]
		return frictionCoeffs.get(color, 0.15)
	
	def getEventAtPoint(self, x:int, y:int) -> int:
		color = self.pixelValues[self.width*y+x]
		return events.get(color, 0)

class TrackManager:
	tracks:list[Track]
	imgs:list[str]
	index:int
	timer:int
	lapTimes:list[int]
	highscore:int
	outputText:str
	fileList:list[str]
	lappingEnabled:bool
	newMap:bool
	
	def __init__(self, fileList:list[str]) -> None:
		self.tracks = []
		self.imgs = []
		for file in fileList:
			self.tracks.append(Track(f"track{file}small.png"))
			self.imgs.append(f"track{file}.png")
		self.index = 0
		self.timer = 0
		self.outputText = "No Scores Yet!"
		self.fileList = fileList
		self._readLB()
		self.newMap = True
		self.lappingEnabled = True

	def _readLB(self) -> None:
		lbFile = open(f"{self.fileList[self.index]}lb.txt", "r")
		laps = []
		for line in lbFile:
			laps.append(int(line))
		lbFile.seek(0, 0)
		self.highscore = int(lbFile.readline())
		self.lapTimes = laps

	def _writeLB(self) -> None:
		lbFile = open(f"{self.fileList[self.index]}lb.txt", "w")
		lbFile.write(str(self.highscore) + "\n")
		laps = self.lapTimes.copy()
		laps.remove(self.highscore)
		for lap in laps:
			lbFile.write(str(lap) + "\n")
		lbFile.close()

	def lap(self) -> None:
		if not self.newMap:
			self.lapTimes.append(self.timer)
			if self.timer < self.highscore:
				self.highscore = self.timer
			self._writeLB()
		else:
			self.newMap = False
		self.lappingEnabled = False
		self.timer = 0
		laps = self.lapTimes
		avg = (laps[-1]+laps[-2]+laps[-3])/3
		self.outputText = f"Best Time: {self.highscore/1000:.2f}secs\nAverage Time: {avg/1000:.2f}secs\nLast Three Times:\n  1: [{laps[-1]/1000:.2f}secs]\n  2: [{laps[-2]/1000:.2f}secs]\n  3: [{laps[-3]/1000:.2f}secs]"

	def screenRefresh(self, screen:_Screen) -> None:
		screen.bgpic(self.imgs[self.index])

	def index(self, newIndex:int) -> None:
		self.index = newIndex
	
	def current(self) -> Track:
		return self.tracks[self.index]
	
	def get(self, index:int) -> Track:
		return self.tracks[index]
	
	def event(self, x:int|tuple, y:int=None) -> int:
		if y is None:
			y = x[1]
			x = x[0]
		x = floor(0.1*x) + 96
		y = floor(-0.1*y) + 54
		return self.current().getEventAtPoint(x, y)
	
	def coeff(self, x:int|tuple, y:int=None) -> float:
		if y is None:
			y = x[1]
			x = x[0]
		x = floor(0.1*x) + 96
		y = floor(-0.1*y) + 54
		return self.current().getCoeffAtPoint(x, y)