from cImage import*

p1 = Pixel(0,255,0)
p2 = Pixel(255,0,0)
im = EmptyImage(300,300)
w = ImageWin("Image",300,300)

# cross lines
for i in range(300):
    im.setPixel(i,150,p1)
    im.setPixel(150,i,p1)

# lower-right diagonal line
for i in range(150):
    im.setPixel(i + 150,i + 150,p2)
 
im.draw(w)
