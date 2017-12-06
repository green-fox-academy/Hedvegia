from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.
def draw(s, c):
    box = canvas.create_rectangle(150-(s/2), 150-(s/2), 150+(s/2), 150+(s/2), fill=c)
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
for i in range(len(colors)):
    box = canvas.create_rectangle(150-(140-i*10), 150-(140-i*10), 150+(140-i*10), 150+(140-i*10), fill=colors[i])
draw(50, 'black')
root.mainloop()