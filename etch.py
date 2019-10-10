# list of necessary imports
import click
from gfxhat import lcd, fonts, backlight
from PIL import Image, ImageFont, ImageDraw
import time

# function to display text on screen
def displayText(text,lcd,x,y):
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold,18)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show()
    time.sleep(1)
    lcd.clear()
    lcd.show()

# function to adjust background color
def changeBackgroundColor(color):
    backColor = True
    while backColor == True:
        if color == "Red":
            backlight.set_all(0,0,0)
            backlight.set_all(255, 0, 0)
            backlight.show()
            break
        elif color == "Green":
            backlight.set_all(0,0,0)
            backlight.set_all(0, 255, 0)
            backlight.show()
            break
        elif color == "Blue":
            backlight.set_all(0,0,0)
            backlight.set_all(0, 0, 255)
            backlight.show()
            break
        elif color == "None":
            backlight.set_all(0,0,0)
            backlight.show()
            break


# main function to create sketches
def etchASketch(a,b):
    displayText(words,lcd,30,20)
    lcd.set_pixel(a,b,2)
    lcd.show()

    active = True
    while active == True:
        c = click.getchar()
        # up arrow
        if c == '\x1b[A':
            b = b - 1
            if b < 0:
                b = 63
        # down arrow
        elif c == '\x1b[B':
            b = b + 1
            if b > 63:
                b = 0

        # right arrow
        elif c == '\x1b[C':
            a = a + 1
            if a > 127:
                a = 0

        # left arrow
        elif c == '\x1b[D':
            a = a - 1
            if a < 0:
                a = 127

        elif c == 's':
            lcd.clear()
            lcd.show()

        # quit program
        elif c == 'q':
            backlight.set_all(0,0,0)
            backlight.show()
            lcd.clear()
            lcd.show()
            break


        lcd.set_pixel(a,b,1)
        lcd.show()


# all variables
words = "Etch a Sketch!"
x = int(input("What X-coordinate would you like to begin at?"))
y = int(input("What Y-coordinate would you like to begin at?"))
choice = input("What color would you like the backlight-Red, Green, Blue, or None?")

# call for function
changeBackgroundColor(choice)
etchASketch(x,y)