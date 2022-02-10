from cImage import*

def red_pixelated(old_pixel):
    red_pixel = old_pixel.getRed() + 100
    return Pixel(red_pixel, old_pixel.getGreen(), old_pixel.getBlue())
    
def red_intensity(image):
    butterfly = FileImage(image)
    width = butterfly.getWidth()
    height = butterfly.getHeight()

    window = ImageWin("red butterfly", width, height)


    for row in range(height):
        for col in range(width):
            old_pixel = butterfly.getPixel(col, row)
            red_pixel = red_pixelated(old_pixel)
            butterfly.setPixel(col, row, red_pixel)

    butterfly.draw(window)

red_intensity("butterfly.gif")
