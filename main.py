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

	image.paste(sprites.write(image, 0), (50, 50))
	image.paste(sprites.write(image, 0), (100, 50))

	disp.image(image)
	disp.display()

