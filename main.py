import Adafruit_SSD1306

import sprites

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
disp.begin()
disp.clear()
disp.display()

font = ImageFont.load_default()

image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)

done = False
while not done:

#	image = Image.new('1', (disp.width, disp.height))
#	draw = ImageDraw.Draw(image)

	image = sprites.write(image, 50, 50, 0)
	image = sprites.write(image, 100, 50, 0)

	disp.image(image)
	disp.display()

