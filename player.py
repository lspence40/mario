import world

class Mario:
	pos = [0, 0]
	vel = [0, 0]
	size = [8, 8]

	def __init__(self, x, y):
		self.pos[0] = x
		self.pos[1] = y

	def getPos(self):
		return (self.pos[0], self.pos[1])

	def roundUp(self, num):
		if num % 1 != 0:
			num += 1
		return int(num)

	def detectGroundUnder(self, x, y, w, h, g):
		x = self.roundUp(x/8)
		y = self.roundUp(y/8)
		w = self.roundUp(w/8)
		h = self.roundUp(h/8)
		for i in range(int(h)):
			for j in range(int(w)):
				if g[y+i][x+j]:
					return True
		return False

	def doGravity(self):
		self.vel[1] -= 4
		if self.detectGroundUnder(self.pos[0], world.worldHeight()-self.pos[1], self.size[0], self.size[1], world.getAll()):
			self.vel[1] = 0
			while self.detectGroundUnder(self.pos[0], world.worldHeight()-self.pos[1], self.size[0], self.size[1], world.getAll()):
				self.pos[1] += 1
				print(abc)
		self.pos[1] -= self.vel[1]

#ground = world.getAll()
#test = Mario(0, 0)
#for i in range(world.worldHeight()*2):
#	for j in range(world.worldWidth()*2):
#		print(int(test.detectGroundUnder(j*4, i*4, 8, 8, ground)), end=' ')
#	print()
