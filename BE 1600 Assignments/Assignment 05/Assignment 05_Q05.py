from cImage import*

''' pixel averages with itself and its neighbors '''
def pixel_smoother(col, row, image):
    middle = image.getPixel(col, row)
    above = image.getPixel (col,     row + 1)
    below = image.getPixel (col,     row - 1)
    left = image.getPixel  (col - 1, row)
    right = image.getPixel (col + 1, row)

    pixel = [middle, above, below, left, right]
    
    red = int(0)
    green = int(0)
    blue = int(0)
    for i in pixel:
        red += i.getRed()
        green += i.getGreen()
        blue += i.getBlue()

    new_red = red // 5
    new_green = green // 5
    new_blue = blue // 5

    return Pixel(new_red, new_green, new_blue)


''' prints old and smoother image '''
def image_smoother(image_file):
    enlarged_image = FileImage(image_file)
    width = enlarged_image.getWidth()
    height = enlarged_image.getHeight()
    im = EmptyImage(width * 2, height)
    w = ImageWin("Smooth Image", width * 2, height)

    enlarged_image.draw(w)

    smooth_image = EmptyImage(width, height)
    for row in range(1, height - 2):
        for col in range(1, width - 2):
            smooth_pixel = pixel_smoother(col, row, enlarged_image)
            smooth_image.setPixel(col + 1, row + 1, smooth_pixel)

    smooth_image.setPosition(width + 1, 0)
    smooth_image.draw(w)
    

image_smoother("pic.gif")
