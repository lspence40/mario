def detectGroundUnder(x, y, w, h, g):
	x = int(x/8)
	y = int(y/8)
	w = int(w/8)
	h = int(h/8)
	for i in range(int(w)):
		for j in range(int(h)):
			if g[x+i][y+j]:
				return True
	return False

w = 8
h = 8
ground = [
[0, 0, 0, 0],
[0, 0, 1, 1],
[1, 1, 1, 1]
]

for i in range(0, len(ground)*8, 8):
	print()
	for j in range(0, len(ground[i//8])*8, 8):
		print(detectGroundUnder(i, j, w, h, ground), end='')
		print(' ' + str(i) + ' ' + str(j))
