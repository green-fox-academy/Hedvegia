from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400', bg='black')
canvas.pack()


line2 = canvas.create_line(0, 200, 0, 400, fill='yellow')
for i in range(10):
    line = canvas.create_line (200, 20+i*20, 180-i*20, 200, fill='yellow')
for i in range(10):
    line = canvas.create_line (200, 20+i*20, 220+i*20, 200, fill='yellow')
for i in range(10):
    line = canvas.create_line (200, 380-i*20, 180-i*20, 200, fill='yellow')
for i in range(10):
    line = canvas.create_line (200, 380-i*20, 220+i*20, 200, fill='yellow')
line = canvas.create_line (200, 0, 200, 400, fill='yellow')

root.mainloop()