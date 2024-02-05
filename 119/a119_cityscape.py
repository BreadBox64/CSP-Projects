from turtle import *
import random
import math

screen = Screen()
screen.colormode(255)

# Turtle Inits
buildingTurtle = Turtle()
buildingTurtle.pu()
buildingTurtle.ht()
#buildingTurtle.speed(0)

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
def redefineBuildingShape(drawTurtle, mode = "floor", usePreviousValues = False, widthX = False, widthZ = False, height = False, wallColor = False, outlineColor = False, window = False):
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
			return 1
		windowColor = oldBuildingShapeVars.windowColor if (usePreviousValues and not window) else window[0] 
		windowScale = oldBuildingShapeVars.windowScale if (usePreviousValues and not window) else (generateWindowScale(window, widthX, widthZ, height) if (type(window) == int) else window[1]) # (A, B, C) A - width of window, B - range 0-1 representing window height, C - num of windows
		wW = windowScale[0] # Window Width
		wH = (wW/2) # Window Half Width
		wQ = (wW/4) # Window Quarter Width
		wS = windowScale[1] * height # Window Scale (height)
		wNumX = windowScale[2]
		for i in range(1, wNumX+1):
			offset = i/(wNumX+1)
			offPos = (-offset*widthX, (offset*halfWidthX)+((height-wS)*0.5))
			buildingWindow.addcomponent([
				vAdd(offPos, (-wH, wS+wQ)),
				vAdd(offPos, (wH, wS-wQ)),
				vAdd(offPos, (wH, -wQ)),
				vAdd(offPos, (-wH, wQ)),
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
	buildingTurtle.st()

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
		for i in range(building[2]):
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
	# 4x4 grid
	wallColors = ["#AAAAAA", "#BBBB99", "#DDCCCC"]
	outlineColors = ["#666666"]
	windowColors = ["#AABBFF"]
	grid = [
		((3, 0), (3, 0), 5, wallColors[0], outlineColors[0], (windowColors[0], (5, 0.6, 3))),
		((0, 0), (1, 1), 2, wallColors[1], outlineColors[0]),
		((0, 2), (0, 3), 7, wallColors[2], outlineColors[0]),
		((0, -1), (0, -2), 20, wallColors[1], outlineColors[0])
	]
	scales = [30, 10, 20]
	return (grid, scales)

# Shape Building Turtle
shapingTurtle = Turtle()

# Main Draw Loop
buildingGrid = initBuildingGrid()
drawBuildingGrid(buildingGrid)
screen.mainloop()