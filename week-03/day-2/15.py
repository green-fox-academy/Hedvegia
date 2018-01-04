from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

for i in range(20):
    lines = canvas.create_line(0, 20+i*20, 20+i*20, 300, fill='yellow')
for i in range(20):
    lines = canvas.create_line(300, 280-i*20, 280-i*20, 0, fill='orange')
root.mainloop()