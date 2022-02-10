# pixel (0,0) will be mapped to pixels
''' (0,0)
    (1,0)
    (0,1)
    (1,1) '''
#pixel (2,2) maps to pixels:
''' (4,4)
    (5,4)
    (4,5)
    (5,5) '''

#general case of a pixel with location (col, row) gives the four pixels
''' (2 * col,     2 * row)
    (2 * col + 1, 2 * row)
    (2 * col,     2 * row + 1)
    (2 * col + 1, 2 * row + 1) '''
# example to help in Assignment 05_Q03
from image import*

def doubleImage(oldImage):
    oldW = oldImage.getWidth()
    oldH = oldImage.getHeight()

    #for the assignment, change for user input
    newIm = EmptyImage(oldW * 2, oldH * 2) 

    for row in range(oldH):
        for col in range(oldW):
            oldPixel = oldImage.getPixel(col, row)

            newIm.setPixel(2 * col, 2 * row, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row, oldPixel)
            newIm.setPixel(2 * col, 2 * row + 1, oldPixel)
            newIm.setPixel(2 * col + 1, 2 * row + 1, oldPixel)

    return newIm

def makeDoubleImage(imageFile):
    oldImage = FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    
    myWin = ImageWin(width * 2, height * 3)
    oldImage.draw(myWin)

    #oldImage.setPosition(0 + width, 0)
    #oldImage.draw(myWin)
    
    newImage = doubleImage(oldImage)
    newImage.setPosition(0, oldImage.getHeight() + 1)
    newImage.draw(myWin)
    
    myWin.exitOnClick()
    
makeDoubleImage("butterfly.gif")
