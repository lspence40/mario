import world

pos = [64, 0]
vel = [0, 0]
size = [8, 8]

def getPos():
	return (pos)

def roundUp(num):
	if num % 1 != 0:
		num += 1
	return int(num)

def detectGroundUnder(x, y, w, h, g):
	x = roundUp(x/8)
	y = roundUp(y/8)
	w = roundUp(w/8)
	h = roundUp(h/8)
	#print(x, end=' ')
	#print(y, end=' ')
	for i in range(int(w)):
		for j in range(int(h)):
			if g[x+i][y+j]:
				return True
	return False

def doGravity():
	global pos
	global vel
	vel[1] -= 23
	if detectGroundUnder(world.worldWidth()-pos[0], world.worldHeight()-pos[1], size[0], size[1], world.getAll()):
		vel[1] = 0
		while detectGroundUnder(world.worldWidth()-pos[0], world.worldHeight()-pos[1], size[0], size[1], world.getAll()):
			pos[1] += 1
	pos[1] -= vel[1]

#ground = world.getAll()
#for i in range(world.worldHeight()):
#	print()
#	for j in range(world.worldWidth()):
#		print(detectGroundUnder(i*8, j*8, 8, 8, ground), end='\t')
#print()
