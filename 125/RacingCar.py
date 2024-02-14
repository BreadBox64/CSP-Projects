import math
from turtle import *
from numpy import cross

def vRotate(vec:Vec2D, angle:float) -> Vec2D:
	rad = math.radians(angle)
	cos = math.cos(rad)
	sin = math.sin(rad)
	return Vec2D(vec[0]*cos + vec[1]*cos, vec[1]*sin + vec[0]*sin)

def vHeading(vec:Vec2D) -> float:
	rad = math.atan2(vec[1], vec[0])
	return math.degrees(rad)

def vMag(vec:Vec2D) -> float:
	return math.sqrt(vec[0]**2 + vec[1]**2)

def vNorm(vec:Vec2D, len:float) -> Vec2D:
	return vec * (len/vMag(vec))

class RacingCar:
	frictionCoeff:float
	pos:Vec2D
	vel:Vec2D
	accInertia:int
	rotInertia:int
	heading:float
	inputs:dict
	
	def __init__(self, _pos:Vec2D=Vec2D(0, 0), _vel:Vec2D=Vec2D(0, 0), _heading:float=0.0, _frictionCoeff:float=0.2) -> None:
		self.pos = _pos
		self.vel = _vel
		self.heading = _heading
		self.frictionCoeff = _frictionCoeff
		self.accInertia = 0.0
		self.rotInertia = 0.0
		self.maxSpeed = 10
		self.inputs = { # lowercase represents the input inertia, capital the condition of the key
			'W': False,
			'A': False,
			'S': False,
			'D': False,
			'Q': False,
			'E': False,
		}

	def _step(self) -> None:
		inputs = self.inputs
		# Input inertia step
		fd = int(inputs['W'])-int(inputs['S']) * 0.01
		if fd != 0:
			self.accInertia += fd if fd + self.accInertia <= 2 and fd + self.accInertia >= -1 else 0 
		else:
			self.accInertia = 0

		rot = (int(inputs['A'])-int(inputs['D'])) * abs(self.accInertia)
		if rot != 0:
			self.rotInertia += rot if rot + self.rotInertia <= 6 and rot + self.rotInertia >= -6 else 0 
		else:
			self.rotInertia = 0

		# Actual physics step
		acc = vRotate((self.accInertia, 0), self.heading)
		#print(str(acc))
		acc -= self.vel * (self.frictionCoeff/(vMag(self.vel) + 1))
		acc -= self.vel * 0.5 * math.sin(math.radians(abs(self.heading - vHeading(self.vel))))
		self.heading += self.rotInertia
		self.vel += acc
		if vMag(self.vel) > self.maxSpeed:
			self.vel = vNorm(self.vel, self.maxSpeed)
		self.pos += self.vel
		
	def draw(self, trtl:Turtle, echo:list[Turtle]) -> None:
		if echo is not None:
			newPos = self.pos
			newHeading = self.heading
			for t in echo:
				oldPos = t.pos()
				oldHeading = t.heading()
				t.goto(newPos)
				t.seth(newHeading)
				newPos = oldPos
				newHeading = oldHeading
		self._step()
		trtl.goto(self.pos)
		trtl.seth(self.heading)

	def inputChanged(self, key:str, val:bool) -> None:
		self.inputs[key] = val
		#print(key)
		if val:
			if key == 'Q':
				self.maxSpeed -= 1 if self.maxSpeed > 0 else 0
			elif key == 'E':
				self.maxSpeed += 1 if self.maxSpeed < 35 else 0