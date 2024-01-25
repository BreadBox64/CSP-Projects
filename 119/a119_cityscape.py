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
	"widthX": 30,
	"widthZ": 30,
	"height": 10,
	"wallColor": "#AAAAAA",
	"outlineColor": "#666666",
	"windowColor": False
}
def redefineBuildingShape(drawTurtle, usePreviousValues = False, widthX = False, widthZ = False, height = False, wallColor = False, outlineColor = False, windowColor = False):
	widthX = oldBuildingShapeVars.widthX if (usePreviousValues and not widthX) else (widthX if widthX else 30)
	widthZ = oldBuildingShapeVars.widthZ if (usePreviousValues and not widthZ) else (widthZ if widthZ else 30)
	height = oldBuildingShapeVars.height if (usePreviousValues and not height) else (height if height else 10)
	wallColor = oldBuildingShapeVars.wallColor if (usePreviousValues and not wallColor) else (wallColor if wallColor else "#AAAAAA")
	outlineColor = oldBuildingShapeVars.outlineColor if (usePreviousValues and not outlineColor) else (outlineColor if outlineColor else "#666666")
	windowColor = oldBuildingShapeVars.windowColor if (usePreviousValues and not windowColor) else windowColor

	buildingFloor = Shape("compound")
	halfWidthX = widthX/2
	halfWidthZ = widthZ/2
	buildingFloor.addcomponent(((0, 0), (widthZ, halfWidthZ), (widthZ, halfWidthZ + height), (0, height), (-widthX, halfWidthX + height), (-widthX, halfWidthX)), wallColor, outlineColor)
	buildingFloor.addcomponent(((0, 0), (0, height)), outlineColor, outlineColor)
	screen.register_shape("buildingFloor", buildingFloor)
	drawTurtle.shape("buildingFloor")

def drawBuildingGrid(buildingGrid):
	grid = buildingGrid[0]
	scales = buildingGrid[1]
	buildingWidth = scales[0]
	buildingHeight = scales[1]
	streetWidth = scales[2]
	halfWidth = buildingWidth/2
	streetHalfWidth = streetWidth/2

	for building in grid:
		offsetX = ((building[0][0] - building[0][1]) * buildingWidth) + (((building[0][0] - building[0][1]) - 1) * streetWidth)
		offsetY = ((building[0][0] + building[0][1]) * halfWidth) + ((building[0][0] + building[0][1] - 1) * streetHalfWidth)
		unitWidthX = (abs(building[0][0] - building[1][0]) + 1)
		widthX = (unitWidthX * buildingWidth) + ((unitWidthX - 1) * streetWidth)
		unitWidthZ = (abs(building[0][1] - building[1][1]) + 1)
		widthZ = (unitWidthZ * buildingWidth) + ((unitWidthZ - 1) * streetWidth)
		buildingTurtle.goto(offsetX, offsetY)
		buildingTurtle.seth(90)
		redefineBuildingShape(buildingTurtle, False, widthX, widthZ, buildingHeight, "#AAAAAA", "#666666")
		for i in range(building[2]):
			buildingTurtle.stamp()
			buildingTurtle.fd(buildingHeight)
		

def initBuildingGrid():
	# 4x4 grid
	wallColors = ["#AAAAAA", "#BBBB99", "#DDCCCC"]
	outlineColors = ["#666666"]
	grid = [
		((3, 0), (3, 0), 5, wallColors[0], outlineColors[0]),
		((0, 0), (1, 1), 2, wallColors[1], outlineColors[0]),
		((0, 2), (0, 3), 7, wallColors[2], outlineColors[0])
	]
	scales = [30, 10, 20]
	return (grid, scales)

# Shape Building Turtle
shapingTurtle = Turtle()

# Main Draw Loop
buildingGrid = initBuildingGrid()
drawBuildingGrid(buildingGrid)
screen.mainloop()