from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='white')
canvas.pack()

# fill the canvas with a checkerboard pattern.
#for i in range(20):
for i in range(30):
    black_box = canvas.create_rectangle (0+(30*i), 0+(30*i), 30+(30*i), 30+(30*i), fill='black')
    black_box = canvas.create_rectangle (60+(30*i), 0+(30*i), 90+(30*i), 30+(30*i), fill='black')
    black_box = canvas.create_rectangle (120+30*i, 0+30*i, 150+30*i, 30+30*i, fill='black')
    black_box = canvas.create_rectangle (180+30*i, 0+30*i, 210+30*i, 30+30*i, fill='black')
    black_box = canvas.create_rectangle (240+30*i, 0+30*i, 270+30*i, 30+30*i, fill='black')
    black_box = canvas.create_rectangle (0+30*i, 60+30*i, 30+30*i, 90+30*i, fill='black')
    black_box = canvas.create_rectangle (0+30*i, 120+30*i, 30+30*i, 150+30*i, fill='black')
    black_box = canvas.create_rectangle (0+30*i, 180+30*i, 30+30*i, 210+30*i, fill='black')
    black_box = canvas.create_rectangle (0+30*i, 240+30*i, 30+30*i, 270+30*i, fill='black')
                
root.mainloop()