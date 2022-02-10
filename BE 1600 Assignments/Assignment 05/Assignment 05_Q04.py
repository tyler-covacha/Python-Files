from cImage import*

''' pixel becomes either black or white '''
def black_and_white_pixel(old_pixel):
    color_sum = (old_pixel.getRed() +
                 old_pixel.getGreen() +
                 old_pixel.getBlue()) / 3
    if color_sum >= 128:
        return Pixel(255, 255, 255)
    else:
        return Pixel(0, 0, 0)

''' prints colored image and black&white image '''
def black_and_white_image(image_file):
    color_butterfly = FileImage(image_file)
    width = color_butterfly.getWidth()
    height = color_butterfly.getHeight()
    im = EmptyImage(width * 2, height)
    w = ImageWin("Black and White", width * 2, height)

    color_butterfly.draw(w)

    bw_butterfly = EmptyImage(width,height)
    for row in range(height):
        for col in range(width):
            bw_pixel = black_and_white_pixel(color_butterfly.getPixel(col,row))
            bw_butterfly.setPixel(col, row, bw_pixel)

    bw_butterfly.setPosition(width + 1, 0)
    bw_butterfly.draw(w)
                                             
            

black_and_white_image("butterfly.gif")
