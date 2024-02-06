from turtle import *
import random
import math

# Screen Setup
screen = Screen()
screen.colormode(255)
size = screen.screensize()
screen.delay(0)
screen.bgcolor("#7CFC00")

# Turtle Setup
buildingTurtle = Turtle()
buildingTurtle.pu()
buildingTurtle.ht()
buildingTurtle.speed(0)

# Vector Addition
def vAdd(*args):
	out = []
	for i in args[0]:
		out.append(0)
	for v in args:
		for i in range(len(out)):
			out[i] += v[i]
	return out

# Building Aid Functions
oldBuildingShapeVars = {
	"widthX": 30,
	"widthZ": 30,
	"height": 10,
	"wallColor": "#AAAAAA",
	"outlineColor": "#666666",
	"windowColor": False
}
# This function changes the turtle shape to match that of the specified mode (floor, roof, or window) this can then be stamped to make drawing faster
def redefineBuildingShape(drawTurtle, mode = "floor", usePreviousValues = False, widthX = False, widthZ = False, height = False, wallColor = False, outlineColor = False, window = False):
	# Variable Init
	widthX = oldBuildingShapeVars.widthX if (usePreviousValues and not widthX) else (widthX if widthX else 30)
	widthZ = oldBuildingShapeVars.widthZ if (usePreviousValues and not widthZ) else (widthZ if widthZ else 30)
	height = oldBuildingShapeVars.height if (usePreviousValues and not height) else (height if height else 10)
	wallColor = oldBuildingShapeVars.wallColor if (usePreviousValues and not wallColor) else (wallColor if wallColor else "#AAAAAA")
	outlineColor = oldBuildingShapeVars.outlineColor if (usePreviousValues and not outlineColor) else (outlineColor if outlineColor else "#666666")
	halfWidthX = widthX/2
	halfWidthZ = widthZ/2

	if mode == "floor":
		buildingFloor = Shape("compound")
		buildingFloor.addcomponent(((0, 0), (widthZ, halfWidthZ), (widthZ, halfWidthZ + height), (0, height), (-widthX, halfWidthX + height), (-widthX, halfWidthX)), wallColor, outlineColor)
		buildingFloor.addcomponent(((0, 0), (0, height)), outlineColor, outlineColor)
		screen.register_shape("buildingFloor", buildingFloor)
		drawTurtle.shape("buildingFloor")
		return 0
	elif mode == "roof":
		buildingRoof = Shape("compound")		
		buildingRoof.addcomponent(((0, 0), (widthZ, halfWidthZ), (widthZ - widthX, halfWidthX + halfWidthZ), (-widthX, halfWidthX)), wallColor, outlineColor)
		screen.register_shape("buildingRoof", buildingRoof)
		drawTurtle.shape("buildingRoof")
		return 0
	elif mode == "window":
		buildingWindow = Shape("compound")
		if not window:
			return 1 # Return non-zero output to signify an error condition
		windowColor = oldBuildingShapeVars.windowColor if (usePreviousValues and not window) else window[0] 
		windowScale = oldBuildingShapeVars.windowScale if (usePreviousValues and not window) else (generateWindowScale(window, widthX, widthZ, height) if (type(window) == int) else window[1]) # (A, B, C, D) A - width of window, B - range 0-1 representing window height, C - num of windows
		wW = windowScale[0] # Window Width
		wH = (wW/2) # Window Half Width
		wQ = (wW/4) # Window Quarter Width
		wS = windowScale[1] * height # Window Scale (height)
		# X Axis Windows
		wNumX = windowScale[2]
		scalerX = 2*(wNumX)
		for i in range(scalerX):
			if i % 2 == 1:
				offset = i/scalerX
				offPos = (-offset*widthX, (offset*halfWidthX)+((height-wS)*0.5))
				buildingWindow.addcomponent([
					vAdd(offPos, (-wH, wS+wQ)),
					vAdd(offPos, (wH, wS-wQ)),
					vAdd(offPos, (wH, -wQ)),
					vAdd(offPos, (-wH, wQ)),
				], windowColor, outlineColor)
		# Z Axis Windows
		wNumZ = windowScale[3]
		scalerZ = 2*(wNumZ)
		for i in range(scalerZ):
			if i % 2 == 1:
				offset = i/scalerZ
				offPos = (offset*widthZ, (offset*halfWidthZ)+((height-wS)*0.5))
				buildingWindow.addcomponent([
					vAdd(offPos, (-wH, -wQ)),
					vAdd(offPos, (-wH, wS-wQ)),
					vAdd(offPos, (wH, wS+wQ)),
					vAdd(offPos, (wH, wQ)),
				], windowColor, outlineColor)
		screen.register_shape("buildingWindow", buildingWindow)
		drawTurtle.shape("buildingWindow")
		return 0

def drawBuildingGrid(buildingGrid):
	grid = buildingGrid[0]
	scales = buildingGrid[1]
	buildingWidth = scales[0]
	buildingHeight = scales[1]
	streetWidth = scales[2]
	halfWidth = buildingWidth/2
	streetHalfWidth = streetWidth/2
	streetQuarterWidth = streetWidth/4
	streetSixthWidth = streetWidth/6
	buildingTurtle.st()

	# Draw roads, this is done earlier to prevent erronous overlapping
	for building in grid:
		# Variable Setup
		offsetX = ((building[0][0] - building[0][1]) * buildingWidth) + (((building[0][0] - building[0][1]) - 1) * streetWidth)
		offsetY = ((building[0][0] + building[0][1]) * halfWidth) + ((building[0][0] + building[0][1] - 1) * streetHalfWidth)
		unitWidthX = (abs(building[0][0] - building[1][0]) + 1)
		widthX = (unitWidthX * buildingWidth) + ((unitWidthX - 1) * streetWidth)
		widthSX =  widthX + streetWidth
		unitWidthZ = (abs(building[0][1] - building[1][1]) + 1)
		widthZ = (unitWidthZ * buildingWidth) + ((unitWidthZ - 1) * streetWidth)
		widthSZ = widthZ + streetWidth
		# Draw Streets
		buildingTurtle.goto(offsetX, offsetY-streetSixthWidth)
		buildingTurtle.color("#666666")
		buildingTurtle.pd()
		buildingTurtle.begin_fill()
		buildingTurtle.goto(offsetX-widthSX, (widthSX/2)+offsetY-streetSixthWidth)
		buildingTurtle.goto(offsetX-widthSX, (widthSX/2)+offsetY-(5*streetSixthWidth))
		buildingTurtle.goto(offsetX, offsetY-(5*streetSixthWidth))
		buildingTurtle.goto(offsetX+widthSZ, (widthSZ/2)+offsetY-(5*streetSixthWidth))
		buildingTurtle.goto(offsetX+widthSZ, (widthSZ/2)+offsetY-streetSixthWidth)
		buildingTurtle.end_fill()
		# Draw Road Markings
		buildingTurtle.color("#CCCC66")
		buildingTurtle.pu()
		buildingTurtle.goto(offsetX-widthX-streetHalfWidth, (widthX/2)+offsetY-streetQuarterWidth)
		buildingTurtle.pd()
		buildingTurtle.goto(offsetX-streetHalfWidth, offsetY-streetQuarterWidth)
		buildingTurtle.pu()
		buildingTurtle.goto(offsetX+streetHalfWidth, offsetY-streetQuarterWidth)
		buildingTurtle.pd()
		buildingTurtle.goto(offsetX+widthZ+streetHalfWidth, (widthZ/2)+offsetY-streetQuarterWidth)
		buildingTurtle.pu()

	# Draw actual buildings
	for building in grid:
		# Variable Setup
		offsetX = ((building[0][0] - building[0][1]) * buildingWidth) + (((building[0][0] - building[0][1]) - 1) * streetWidth)
		offsetY = ((building[0][0] + building[0][1]) * halfWidth) + ((building[0][0] + building[0][1] - 1) * streetHalfWidth)
		unitWidthX = (abs(building[0][0] - building[1][0]) + 1)
		widthX = (unitWidthX * buildingWidth) + ((unitWidthX - 1) * streetWidth)
		unitWidthZ = (abs(building[0][1] - building[1][1]) + 1)
		widthZ = (unitWidthZ * buildingWidth) + ((unitWidthZ - 1) * streetWidth)
		wallColor = building[3]
		outlineColor = building[4]
		window = building[5] if len(building) > 5 else False
		# Draw Floors
		buildingTurtle.goto(offsetX, offsetY)
		buildingTurtle.seth(90)
		redefineBuildingShape(buildingTurtle, "floor", False, widthX, widthZ, buildingHeight, wallColor, outlineColor)
		for i in range(building[2]): # Stamp the 
			buildingTurtle.stamp()
			buildingTurtle.fd(buildingHeight)
		# Draw Windows
		if window:
			redefineBuildingShape(buildingTurtle, "window", False, widthX, widthZ, buildingHeight, wallColor, outlineColor, window)
			buildingTurtle.goto(offsetX, offsetY)
			buildingTurtle.seth(90)
			for i in range(building[2]):
				buildingTurtle.stamp()
				buildingTurtle.fd(buildingHeight)
		# Draw Roof
		redefineBuildingShape(buildingTurtle, "roof", False, widthX, widthZ, buildingHeight, wallColor, outlineColor)
		buildingTurtle.stamp()
		buildingTurtle.ht()

def initBuildingGrid():
	wallColorsTall = ["#AAAAAA", "#BBAAAA", "#DDCCCC", "#AAAABB", "#CCCCDD", "#CCCCCC"]
	wallColorsShort = ["#FFCCBB", "#DDD0BB", "#DDCCCC", "#CCCCCC"]
	outlineColors = ["#666666", "#777777"]
	windowColors = ["#AABBFF", "#99AADD", "#8899CC"]
	"""grid = [
		((3, 0), (3, 0), 5, wallColors[0], outlineColors[0], (windowColors[0], (5, 0.6, 4, 4))),
		((0, 0), (1, 1), 2, wallColors[1], outlineColors[0]),
		((0, 2), (0, 3), 7, wallColors[2], outlineColors[0]),
		((0, -1), (0, -2), 20, wallColors[1], outlineColors[0])
	]"""
	pairsWidth = size[0]/50
	grid = []
	for sum in range(int((pairsWidth*2) - 1), -1, -1): # Setting up the for loop this way pre-sorts the list back to front, meaning no additional sorting is needed before drawing
		for x in range(sum + 1): # Get all number pairs for that sum
			pos = (x, sum-x)
			pos = vAdd(pos, (-math.ceil(pairsWidth/2), -math.ceil(pairsWidth/2)))
			floors = math.floor(random.gauss(10, 5))
			floors = floors if floors > 0 else 1
			wallColor = random.choice(wallColorsShort) if floors < 5 else random.choice(wallColorsTall)
			windows = random.choice([4, 4, 3, 2, 0]) if floors < 5 else 4
			window = (random.choice(windowColors), (random.choice([4, 5, 6]), random.choice([0.5, 0.6, 0.7, 0.8, 0.9, 1.0]), windows, (windows if windows != 0 else 2)))
			building = (pos, pos, floors, wallColor, random.choice(outlineColors), window)
			grid.append(building)

	scales = [32, 10, 18] # (width, height, street width)
	return (grid, scales)

# Shape Building Turtle
shapingTurtle = Turtle()

# Main Draw Loop
buildingGrid = initBuildingGrid()
drawBuildingGrid(buildingGrid)
screen.mainloop()