from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

box = canvas.create_rectangle(0, 0, 15, 15, fill='pink')
box1 = canvas.create_rectangle(15, 15, 45, 45, fill='pink')
box2 = canvas.create_rectangle(45, 45, 90, 90, fill='pink')
box3 = canvas.create_rectangle(90, 90, 150, 150, fill='pink')
box4 = canvas.create_rectangle(150, 150, 225, 225, fill='pink')

for i in range(5):
    boxes_with_loop = canvas.create_rectangle(0, 0, 15, 15, fill='pink')
root.mainloop()