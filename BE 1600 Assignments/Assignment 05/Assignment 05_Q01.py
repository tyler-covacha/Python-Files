import math
from cImage import*

p2 = Pixel(255,0,0)
im = EmptyImage(500,500)
w = ImageWin("Circle",300,300)

for x in range(1440):
    im.setPixel(int(math.cos(x) * 100) + 150, int(math.sin(x) * 100) + 150, p2)
im.draw(w)
