from PIL import Image
from math import floor

frictionCoeffs = {
	(0, 0, 0, 255): 0.15,
	(64, 64, 64, 255): 0.15,
	(128, 128, 128, 255): 0.15,
	(255, 255, 255, 255): 0.15,
	(32, 128, 32, 255): 0.4,
	(128, 0, 0, 255): 0.15,
	(255, 0, 0, 255): 0.15,
}

events = {
	(0, 0, 0, 255): 0,
	(64, 64, 64, 255): 0,
	(128, 128, 128, 255): 0,
	(255, 255, 255, 255): 0,
	(32, 128, 32, 255): 0,
	(128, 0, 0, 255): 0,
	(255, 0, 0, 255): 1,
}

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
		return frictionCoeffs.get(color)
	
	def getEventAtPoint(self, x:int, y:int) -> int:
		color = self.pixelValues[self.width*y+x]
		return events.get(color)

class TrackManager:
	tracks:list[Track]
	index:int
	
	def __init__(self, fileList:list[str]) -> None:
		self.tracks = []
		for file in fileList:
			self.tracks.append(Track(file))
		self.index = 0

	def index(self, newIndex:int) -> None:
		self.index = newIndex
	
	def current(self) -> Track:
		return self.tracks[self.index]
	
	def get(self, index:int) -> Track:
		return self.tracks[index]
	
	def lap(self, x:int|tuple, y:int=None) -> bool:
		if y is None:
			y = x[1]
			x = x[0]
		x = floor(0.1*x + 96)
		y = floor(-0.1*y + 96)
		return (self.current().getEventAtPoint(x, y) == 1)
	
	def coeff(self, x:int|tuple, y:int=None) -> float:
		if y is None:
			y = x[1]
			x = x[0]
		x = floor((0.1*x) + 96)
		y = floor((-0.1*y) + 54)
		return self.current().getCoeffAtPoint(x, y)