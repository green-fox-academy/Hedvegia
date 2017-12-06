from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
teal_line1 = canvas.create_line(5, 5, 100, 5, fill='black')
teal_line2 = canvas.create_line(100, 5, 100, 100, fill='red')
teal_line3 = canvas.create_line(100, 100, 5, 100, fill='green')
teal_line4 = canvas.create_line(5, 100, 5, 5, fill='blue')

root.mainloop()