import turtle
import random
import math

screen = turtle.Screen()
screen.colormode(255)

# Building Aid Functions
oldBuildingShapeVars = {
	"width": 30,
	"height": 10,
	"wallColor": "#AAAAAA",
	"outlineColor": "#666666",
	"windowColor": False
}
def redefineBuildingShape(usePreviousValues = False, width = False, height = False, wallColor = False, outlineColor = False, windowColor = False):
	width = oldBuildingShapeVars.width if (usePreviousValues and not width) else (width if width else 30)
	height = oldBuildingShapeVars.height if (usePreviousValues and not height) else (height if height else 10)
	wallColor = oldBuildingShapeVars.wallColor if (usePreviousValues and not wallColor) else (wallColor if wallColor else "#AAAAAA")
	outlineColor = oldBuildingShapeVars.outlineColor if (usePreviousValues and not outlineColor) else (outlineColor if outlineColor else "#666666")
	windowColor = oldBuildingShapeVars.windowColor if (usePreviousValues and not windowColor) else windowColor

	buildingFloor = turtle.Shape("compound")
	halfWidth = width/2
	buildingFloor.addcomponent(((0, 0), (width, halfWidth), (width, halfWidth + height), (0, height), (-width, halfWidth + height), (-width, halfWidth)), wallColor, outlineColor)
	buildingFloor.addcomponent(((0, 0), (0, height)), outlineColor, outlineColor)
	screen.register_shape("buildingFloor", buildingFloor)

# Init Building Turtle
redefineBuildingShape(False, 30, 10, "#AAAAAA", "#666666")
buildingTurtle = turtle.Turtle()
buildingTurtle.shape("buildingFloor")
buildingTurtle.pu()
buildingTurtle.seth(90)
buildingTurtle.stamp()
buildingTurtle.fd(10)
buildingTurtle.stamp()

screen.mainloop()