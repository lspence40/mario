import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

def getSize(id):
	return len(sprites[id][0]), len(sprites[id])

def write(id):
	imageAdd = Image.new('1', (len(sprites[id][0]), len(sprites[id])))
	draw = ImageDraw.Draw(imageAdd)

	for i in range(len(sprites[id])):
		for j in range(len(sprites[id][i])):
			draw.point((i, j), sprites[id][j][i])
	return imageAdd

sprites = [
[
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]
],
[
[0, 1, 1, 1, 1, 1, 1, 0],
[1, 0, 1, 1, 1, 1, 0, 1],
[1, 1, 0, 1, 1, 0, 1, 1],
[1, 1, 1, 0, 0, 1, 1, 1],
[1, 1, 1, 0, 0, 1, 1, 1],
[1, 1, 0, 1, 1, 0, 1, 1],
[1, 0, 1, 1, 1, 1, 0, 1],
[0, 1, 1, 1, 1, 1, 1, 0]
],
[
[1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 0, 1],
[1, 1, 1, 1, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 1, 1, 1, 1],
[1, 1, 0, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0]
],
[
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 0],
[0, 1, 1, 0, 0, 1, 1, 0],
[1, 1, 1, 0, 0, 1, 1, 1]
]
]
