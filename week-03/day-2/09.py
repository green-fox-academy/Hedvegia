from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.
def draw(l):
    box = canvas.create_rectangle (10, 10, 10+l, 10+l, fill='white')
draw(100)
root.mainloop()