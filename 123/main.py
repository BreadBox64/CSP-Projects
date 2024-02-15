#   a123_apple_1.py
import turtle as trtl
from types import FunctionType
import random

#-----setup-----
appleImage = "123/apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("123/background.gif")
#wn.delay(0)
wn.setup(607, 406)
wn.addshape(appleImage) # Make the screen aware of the new file
halfWidth = 275
halfHeight = 175

apple = trtl.Turtle()
apple.shape(appleImage)
apple.pu()

keys = ['_']
for i in range(26):
	keys.append(chr(i+97))

font = (("Arial", 48, "bold"))
currentKey:str = '_'

def newKey():
	currKey = globals()['currentKey']
	apple.clear()
	apple.speed(3)
	apple.goto(apple.xcor(), (-64)-halfHeight)
	apple.speed(0)
	keys.remove(currKey)
	if len(keys) == 0:
		apple.goto(0, 0)
		apple.write("You Win!", False, "center", font)
		def f(x, y):
			exit()
		wn.onclick(f)
		apple.goto(0, -64)
	else:
		currKey = random.choice(keys)
		pos = (random.randint(-halfWidth, halfWidth), random.randint(-halfHeight, halfHeight))
		apple.goto(pos[0], pos[1]-36)
		apple.write(currKey, False, "center", font)
		apple.goto(pos)
		globals()['currentKey'] = currKey

def genListener(key:str) -> FunctionType:
	def f():
		currKey = globals()['currentKey']
		if key == currKey:
			wn.onkeyrelease(None, key)
			newKey()
		wn.listen()
	return f

keyFuncs = []
for key in keys:
	keyFuncs.append(genListener(key))

wn.listen()
for i,f in enumerate(keyFuncs):
	wn.onkeyrelease(f, keys[i])

#-----function calls-----
newKey()

wn.listen()
wn.mainloop()