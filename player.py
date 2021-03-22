import world

xPos = 64
xVel = 0
yPos = 0
yVel = 0

def getPos():
	return (xPos, yPos)

def detectBlockUnder():
	x = int(xPos/8)
	y = int(yPos/8)

	if not world.get(y, x) == 0:
#		print(1)
		return True
#	print(0)
	return False

def doGravity():
	global yVel
	global yPos
	yPos -= yVel
	yVel -= 2

	if detectBlockUnder():
		yVel = 0
		while detectBlockUnder():
			yPos += 1
