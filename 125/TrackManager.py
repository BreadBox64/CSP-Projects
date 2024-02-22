from PIL import Image
from math import floor
from turtle import _Screen
from os import path

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
		self.img = img
		self.pixelValues = list(img.getdata())

	def getCoeffAtPoint(self, x:int, y:int) -> float:
		color = self.pixelValues[192*y+x]
		return frictionCoeffs.get(color, 0.15)
	
	def getEventAtPoint(self, x:int, y:int) -> int:
		color = self.pixelValues[192*y+x]
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
	scale:list[int]
	
	def __init__(self, scale:list[int], fileList:list[str]) -> None:
		self.tracks = []
		self.imgs = []
		self.scale = scale
		for file in fileList:
			self.tracks.append(Track(f"track{file}.png"))
			scaleImg = f"track{file}_{scale[0]}.png"
			if not path.isfile(scaleImg):
				img = Image.open(f"track{file}.png")
				img.resize((192*scale[0], 108*scale[0]), Image.Resampling.NEAREST).save(scaleImg)
			self.imgs.append(scaleImg)
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
		y *= -1
		x = floor((x + self.scale[3])/self.scale[0])
		y = floor((y + self.scale[4])/self.scale[0])
		return self.current().getEventAtPoint(x, y)
	
	def coeff(self, x:int|tuple, y:int=None) -> float:
		if y is None:
			y = x[1]
			x = x[0]
		y *= -1
		x = floor((x + self.scale[3])/self.scale[0])
		y = floor((y + self.scale[4])/self.scale[0])
		return self.current().getCoeffAtPoint(x, y)