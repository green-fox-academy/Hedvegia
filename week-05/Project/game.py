from tkinter import *
from pygame import mixer

mixer.init()
mixer.music.load('troi.mp3')
mixer.music.play()
mixer.music.rewind()


root = Tk()

canvas = Canvas(root, width='720', height='720')



class Map(object):
    def __init__ (self):
        self.tile = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.wall_or_tile = [[True, True, True, False, True, False, True, True, True, True], 
                            [True, True, True, False, True, False, True, False, False, True],
                            [True, False, False, False, True, False, True, False, False, True],
                            [True, True, True, True, True, False, True, True, True, True],
                            [False, False, False, False, True, False, False, False, False, True],
                            [True, False, True, False, True, True, True, True, False, True],
                            [True, False, True, False, True, False, False, True, False, True],
                            [True, True, True, True, True, False, False, True, False, True],
                            [True, False, False, False, True, True, True, True, False, True],
                            [True, True, True, False, True, False, True, True, True, True]]

    def background_tiles(self, x, y):
        for i in range(len(self.wall_or_tile)):
            for j in range(len(self.wall_or_tile[i])):
                if self.wall_or_tile[i][j] is True:
                    canvas.create_image(x+j*72, y+i*72, image=self.tile)
                else:
                    canvas.create_image(x+j*72, y+i*72, image=self.wall)


class Hero(object):
    def __init__(self):
        self.my_hero = PhotoImage(file="hero-down.png")
        self.x = 36
        self.y = 36
        canvas.create_image(self.x, self.y, image=self.my_hero)

    def on_key_press(self, e):
        if e.keysym == "Up":
            if self.y >= 72:
                self.y -= 72
                self.my_hero = PhotoImage(file="hero-up.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-up.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)

        elif e.keysym == "Down":
            if self.y <= 648:
                self.y += 72
                self.my_hero = PhotoImage(file="hero-down.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-down.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)

        elif e.keysym == "Left":
            if self.x >= 72:
                self.x -= 72
                self.my_hero = PhotoImage(file="hero-left.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-left.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)

        elif e.keysym == "Right":
            if self.x < 648:
                self.x += 72
                self.my_hero = PhotoImage(file="hero-right.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-right.png")
                canvas.create_image(self.x, self.y, image=self.my_hero)
    

background = Map()
background.background_tiles(36, 36)
hero = Hero()
canvas.bind("<KeyPress>", hero.on_key_press)
canvas.pack()
canvas.focus_set()
root.mainloop()