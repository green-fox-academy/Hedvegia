from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

filename = PhotoImage(file = "graphic.png")
image = canvas.create_image(0, 0, anchor=NW, image=filename)

root.mainloop()