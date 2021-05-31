import world

pos = [64, 0]
vel = [0, 0]
size = [8, 8]

def getPos():
	return (pos)

def getPlayerXY():
	return playerXY

def roundUp(num):
	if num % 1 != 0:
		num += 1
	return int(num)

def detectGroundUnder(x, y, w, h, g):
	x = roundUp(x/8)
	y = roundUp(y/8)
	w = roundUp(w/8)
	h = roundUp(h/8)
	for i in range(int(h)):
		for j in range(int(w)):
			if g[y+i][x+j]:
				return True
	return False

def doGravity():
	global pos
	global vel
	vel[1] -= 4
	if detectGroundUnder(pos[0], world.worldHeight()-pos[1], size[0], size[1], world.getAll()):
		vel[1] = 0
		print(0)
		while detectGroundUnder(pos[0], world.worldHeight()-pos[1], size[0], size[1], world.getAll()):
			pos[1] += 1
			print(1)
	pos[1] -= vel[1]

#ground = world.getAll()
#for i in range(world.worldHeight()):
#	for j in range(world.worldWidth()):
#		print(int(detectGroundUnder(j*8, i*8, 8, 8, ground)), end=' ')
#	print()
