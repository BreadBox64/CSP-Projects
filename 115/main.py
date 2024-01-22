#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "115\\robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

sets = [
  {'img': "115\maze1.png", 'cmds': [0,0,0,0,1,1,1,1]},
  {'img': "115\maze2.png", 'cmds': [0,0,0,1,1]},
  {'img': "115\maze3.png", 'cmds': [1,0,0,1,1,0,0,1]}
]

######################################
maze = 2 # Set to maze number
#####################################

maze -= 1
wn.bgpic(sets[maze]['img'])
commands = sets[maze]['cmds']

direction = 0

for i in commands:
  while i != direction:
    turn_left()
    direction -= 1
    if direction < 0:
      direction = 3
  move()

wn.mainloop()
