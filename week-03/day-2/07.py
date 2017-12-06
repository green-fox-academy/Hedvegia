from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
box1 = canvas.create_rectangle (150, 150, 190, 190, fill='yellow')
box2 = canvas.create_rectangle (150, 150, 50, 50, fill='green')
box3 = canvas.create_rectangle (150, 150, 100, 200, fill= 'blue')
box4 = canvas.create_rectangle (150, 150, 170, 130, fill='white')

root.mainloop()