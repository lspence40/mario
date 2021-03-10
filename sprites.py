import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

#image = Image.new('1', (disp.width, disp.height))
#draw = ImageDraw.Draw(image)

def write(image, x, y, id):
	imageAdd = Image.new('1', (disp.width, disp.height))
	draw = ImageDraw.Draw(imageAdd)

	for i in range(len(sprites[id])):
		for j in range(len(sprites[id][i])):
			draw.point((x+i, y+j), sprites[id][i][j])
	return imageAdd

#	disp.image(image)
#	disp.display()

sprites = [
[
[255, 255, 255, 255, 255, 0,   255, 255],
[255, 255, 255, 255, 255, 0,   255, 255],
[255, 255, 255, 255, 255, 0,   255, 255],
[255, 255, 255, 255, 255, 0,   255, 255],
[0,   0,   0,   0,   0,   0,   0,   0],
[255, 255, 0,   255, 255, 255, 255, 255],
[255, 255, 0,   255, 255, 255, 255, 255],
[255, 255, 0,   255, 255, 255, 255, 255]
]
]
