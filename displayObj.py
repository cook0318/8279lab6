# necessary module imports
from gfxhat import lcd

# w = the position of the number within the line
# c = the position of the line within the object
# main function that sets pixel based on given list
def displayObj(obj,x,y):
    c = 0
    while c <= len(obj) - 1:
        w = 0
        while w <= len(obj[c]) - 1:
            if obj[c][w] == 1:
                lcd.set_pixel(x,y,1)
                lcd.show()
                w += 1
                x += 1
            else:
                w += 1
                x += 1
                continue
        x = x - len(obj[c])
        y += 1
        c += 1


# possible objects
f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [
[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]


# necessary inputs
x = int(input("What X-coordinate would you like the drawing to begin at?"))
y = int(input("What Y-coordinate would you like the drawing to begin at?"))
choice = input("Which object would you like to draw? Type 'f1' for fighter jet, or 'pm' for Pac-Man.")

if choice == 'f1':
    choice = f1
elif choice == 'pm':
    choice = pm

# function call
displayObj(choice,x,y)