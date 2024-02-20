import math
from turtle import *
from TrackManager import TrackManager

sign = lambda x: math.copysign(1, x)

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
	pos:Vec2D
	vel:Vec2D
	accInertia:int
	rotInertia:int
	heading:float
	inputs:dict
	gearing:int
	gearings = [[5, 5.0], [8, 3.5], [12, 2.5], [16, 1.75], [18, 1.2], [20, 1.0], [25, 0.9], [30, 0.8], [35, 0.75]]
	trackManager:TrackManager
	
	def __init__(self, _pos:Vec2D=Vec2D(0, 0), _vel:Vec2D=Vec2D(0, 0), _heading:float=0.0, _trackManager:TrackManager=None) -> None:
		self.pos = _pos
		self.vel = _vel
		self.heading = _heading
		self.rotInertia = 0.0
		self.gearing = 5
		self.maxSpeed = self.gearings[self.gearing][0]
		self.accMult = self.gearings[self.gearing][1]
		self.inputs = {
			'W': False,
			'A': False,
			'S': False,
			'D': False,
			'Q': False,
			'E': False,
			'Space': False,
		}
		if _trackManager is None:
			self.frictionCoeff = lambda _: 0.1
			self.trackManager = False
		else:
			self.frictionCoeff = _trackManager.coeff
			self.trackManager = _trackManager
	
	def _recalcGearing(self) -> None:
		self.maxSpeed = self.gearings[self.gearing][0]
		self.accMult = self.gearings[self.gearing][1]
	
	def _handleBounds(self) -> None:
		pos = self.pos
		vel = self.vel
		if pos[0] < -960:
			pos = Vec2D(-960, pos[1])
			vel = Vec2D(0, vel[1])
		elif pos[0] > 960:
			pos = Vec2D(960, pos[1])
			vel = Vec2D(0, vel[1])
		if pos[1] < -540:
			pos = Vec2D(pos[0], -540)
			vel = Vec2D(vel[0], 0)
		elif pos[1] > 540:
			pos = Vec2D(pos[0], 540)
			vel = Vec2D(vel[0], 0)
		self.pos = pos
		self.vel = vel

	def _handleEvents(self) -> None:
		if self.trackManager:
			pos = self.pos
			tm = self.trackManager
			event = tm.event(pos)
			match event:
				case 0:
					return
				case 1:
					pass #tm.lap()
				case 2:
					pass #tm.fail()

	def _step(self) -> None:
		inputs = self.inputs
		# Input inertia step
		fd = int(inputs['W'])-int(inputs['S']) * 0.005 * self.accMult
		print(int(inputs['Space']))
		rot = (int(inputs['A'])-int(inputs['D'])) * (1+int(inputs['Space'])) * int(inputs['W'])-int(inputs['S']) * self.accMult
		#print(self.rotInertia)
		self.rotInertia += rot
		self.rotInertia = self.rotInertia if self.rotInertia <= 60 else 60
		self.rotInertia = self.rotInertia if self.rotInertia >= -60 else -60

		# Actual physics step
		acc = vRotate((fd, 0), self.heading)
		frictionCoeff = self.frictionCoeff(self.pos)
		#print(f"{self.pos} - {self.frictionCoeff(self.pos)}")
		acc -= self.vel * frictionCoeff
		angleMult = math.sin(math.radians(abs(self.heading - vHeading(self.vel))))
		acc -= self.vel * 0.1 * angleMult
		self.heading += self.rotInertia*0.1*(1+0.4*int(inputs['Space']))
		self.vel += acc
		if vMag(self.vel) > self.maxSpeed:
			self.vel = vNorm(self.vel, self.maxSpeed)
		self.pos += self.vel
		self._handleBounds()
		self._handleEvents()
		if self.rotInertia != 0:
			self.rotInertia = sign(self.rotInertia) * math.floor(abs(self.rotInertia) - 1)
		
	def draw(self, trtl:Turtle, echo:list[Turtle] = None) -> None:
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
		if val:
			if key == 'Q':
				self.gearing -= 1 if self.gearing > 0 else 0
				self._recalcGearing()
			elif key == 'E':
				self.maxSpeed += 1 if self.maxSpeed + 1 < len(self.gearings) else 0
				self._recalcGearing()