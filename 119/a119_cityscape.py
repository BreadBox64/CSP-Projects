from turtle import *
import random
import math

screen = Screen()
screen.colormode(255)

# Turtle Inits
buildingTurtle = Turtle()
buildingTurtle.pu()

# Building Aid Functions
oldBuildingShapeVars = {
	"width": 30,
	"height": 10,
	"wallColor": "#AAAAAA",
	"outlineColor": "#666666",
	"windowColor": False
}
def redefineBuildingShape(drawTurtle, usePreviousValues = False, width = False, height = False, wallColor = False, outlineColor = False, windowColor = False):
	width = oldBuildingShapeVars.width if (usePreviousValues and not width) else (width if width else 30)
	height = oldBuildingShapeVars.height if (usePreviousValues and not height) else (height if height else 10)
	wallColor = oldBuildingShapeVars.wallColor if (usePreviousValues and not wallColor) else (wallColor if wallColor else "#AAAAAA")
	outlineColor = oldBuildingShapeVars.outlineColor if (usePreviousValues and not outlineColor) else (outlineColor if outlineColor else "#666666")
	windowColor = oldBuildingShapeVars.windowColor if (usePreviousValues and not windowColor) else windowColor

	buildingFloor = Shape("compound")
	halfWidth = width/2
	buildingFloor.addcomponent(((0, 0), (width, halfWidth), (width, halfWidth + height), (0, height), (-width, halfWidth + height), (-width, halfWidth)), wallColor, outlineColor)
	buildingFloor.addcomponent(((0, 0), (0, height)), outlineColor, outlineColor)
	screen.register_shape("buildingFloor", buildingFloor)
	drawTurtle.shape("buildingFloor")

def drawBuildingGrid(buildingGrid):
	grid = buildingGrid[0]
	scales = buildingGrid[1]
	buildingWidth = scales[0]
	buildingHeight = scales[1]
	streetWidth = scales[2]

	for building in grid:
		offsetX = (building[0][0] * buildingWidth) + ((building[0][0] - 1) * streetWidth)
		offsetY = (building[0][1] * buildingWidth) + ((building[0][1] - 1) * streetWidth)
		widthX = (building[1][0] * buildingWidth) + ((building[1][0] - 1) * streetWidth) - offsetX
		widthY = (building[1][1] * buildingWidth) + ((building[1][1] - 1) * streetWidth) - offsetY
		buildingTurtle.goto(offsetX, offsetY)
		

def initBuildingGrid():
	# 4x4 grid
	wallColors = ["#AAAAAA", "#BBBB99", "#DDCCCC"]
	outlineColors = ["#666666"]
	grid = [
		((-3, 0), (-3, 0), 5, wallColors[0], outlineColors[0]),
		((0, 0), (-1, -1), 2, wallColors[2], outlineColors[0]),
	]
	scales = [30, 10, 20]
	return (grid, scales)

# Shape Building Turtle
shapingTurtle = Turtle()

# Init Building Turtle5

redefineBuildingShape(buildingTurtle, False, 30, 10, "#AAAAAA", "#666666")
buildingTurtle.pu()
buildingTurtle.seth(90)
buildingTurtle.stamp()
buildingTurtle.fd(10)
buildingTurtle.stamp()

screen.mainloop()