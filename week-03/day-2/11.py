from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

for i in range(1,19):
    box = canvas.create_rectangle (5 + (15*i), 5 + (15*i), 20 + (15*i), 20 + (15*i), fill='pink')


root.mainloop()