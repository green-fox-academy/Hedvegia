from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400', bg='black')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]


for i in range(1, 12):
    lines = canvas.create_line(0, 180-20*i, 0+i*20, 0, fill='yellow')
for i in range(1,11):
    line = canvas.create_line (200-i*20, 200, 200, 0+i*20, fill='yellow')
for i in range(1,11):
    line = canvas.create_line (200+i*20, 200, 200, 0+i*20,  fill='yellow')
for i in range(1,11):
    line = canvas.create_line (200, 400-i*20, 200-i*20, 200, fill='yellow')
for i in range(1,11):
    line = canvas.create_line (200, 400-i*20, 200+i*20, 200, fill='yellow')




root.mainloop()