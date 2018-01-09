from tkinter import *
from pygame import mixer
import random

class Map(object):
    def __init__ (self):
        self.x = 0
        self.y = 0
        self.tile = PhotoImage(file = "floor.png")
        self.wall = PhotoImage(file = "wall.png")
        self.wall_or_tile = [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                            [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                            [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
                            [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                            [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0]]

    def background_tiles(self):
        for i in range(len(self.wall_or_tile)):
            for j in range(len(self.wall_or_tile[i])):
                if self.wall_or_tile[i][j] is 0:
                    canvas.create_image(self.x+j*72, self.y+i*72, anchor=NW, image=self.tile)
                else:
                    canvas.create_image(self.x+j*72, self.y+i*72, anchor=NW, image=self.wall)

    def draw_map(self):
        self.background_tiles()


class Hero(object):
    def __init__(self):
        self.my_hero = PhotoImage(file="hero-down.png")
        self.x = 0 
        self.y = 0 
        canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)

    def on_key_press(self, e):
        if e.keysym == "Up":
            if self.y >= 72 and background.wall_or_tile[(self.y-72)//72][(self.x)//72] == 0:
                self.y -= 72
                self.my_hero = PhotoImage(file="hero-up.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-up.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)

        elif e.keysym == "Down":
            if self.y <= 576 and background.wall_or_tile[(self.y+72)//72][(self.x)//72] == 0:
                self.y += 72
                self.my_hero = PhotoImage(file="hero-down.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-down.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)

        elif e.keysym == "Left":
            if self.x >= 72 and background.wall_or_tile[(self.y)//72][(self.x-72)//72] == 0:
                self.x -= 72
                self.my_hero = PhotoImage(file="hero-left.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-left.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)

        elif e.keysym == "Right":
            if self.x <= 576 and background.wall_or_tile[(self.y)//72][(self.x+72)//72] == 0:
                self.x += 72
                self.my_hero = PhotoImage(file="hero-right.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)
            else:
                self.my_hero = PhotoImage(file="hero-right.png")
                canvas.create_image(self.x, self.y, anchor=NW, image=self.my_hero)  


class Enemy(object):
    def __init__(self, x = 0, y = 0):
        self.x = 0
        self.y = 0


class Angry_clouds(Enemy):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.angry_clouds = PhotoImage(file='angry_clouds.png')

    def angry_clouds_draw(self):
        self.x = random.randrange(72, 576, 72)
        self.y = random.randrange(0, 576, 72)
        if background.wall_or_tile[self.y//72][self.x//72] == 0:
            canvas.create_image(self.x, self.y, anchor=NW, image=self.angry_clouds)
        else:
            return self.angry_clouds_draw()
        
    def angry_clouds_move(self, e):
        if e.keysym == "Right" or e.keysym == "Left" or e.keysym == "Up" or e.keysym == "Down":

                t = random.randint(1, 5)

                if t == 1:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.x <= 576 and background.wall_or_tile[(self.y)//72][(self.x+72)//72] == 0:
                        self.x += 72
                        self.angry_clouds = PhotoImage(file="angry_clouds")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)

                elif t == 2:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.x >= 72 and background.wall_or_tile[(self.y)//72][(self.x-72)//72] == 0:
                        self.x -= 72
                        self.angry_clouds = PhotoImage(file="angry_clouds.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)

                elif t == 3:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.y <= 576 and background.wall_or_tile[(self.y+72)//72][(self.x)//72] == 0:
                        self.y += 72
                        self.angry_clouds = PhotoImage(file="angry_clouds.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)

                elif t == 3:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.y >= 72 and background.wall_or_tile[(self.y-72)//72][(self.x)//72] == 0:
                        self.y -= 72
                        self.angry_clouds = PhotoImage(file="angry_clouds.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)


class Boss(Enemy):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self.boss = PhotoImage(file="boss.png")

    def boss_draw(self):
        self.x = random.randrange(144, 576, 72)
        self.y = random.randrange(144, 576, 72)
        if background.wall_or_tile[self.y//72][self.x//72] == 0:
            canvas.create_image(self.x, self.y, anchor=NW, image=self.boss)
        else:
            return self.boss_draw()

    def boss_move(self, e):
        if e.keysym == "Right" or e.keysym == "Left" or e.keysym == "Up" or e.keysym == "Down":

                t = random.randint(1, 5)

                if t == 1:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.x <= 576 and background.wall_or_tile[(self.y)//72][(self.x+72)//72] == 0:
                        self.x += 72
                        self.boss = PhotoImage(file="boss.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)

                elif t == 2:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.x >= 72 and background.wall_or_tile[(self.y)//72][(self.x-72)//72] == 0:
                        self.x -= 72
                        self.boss = PhotoImage(file="boss.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)

                elif t == 3:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.y <= 576 and background.wall_or_tile[(self.y+72)//72][(self.x)//72] == 0:
                        self.y += 72
                        self.boss = PhotoImage(file="boss.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)

                elif t == 3:
                    print("kaka ez a játék, ha nem mozognak a szörnyecskéim:(")
                    if self.y >= 72 and background.wall_or_tile[(self.y-72)//72][(self.x)//72] == 0:
                        self.y -= 72
                        self.boss = PhotoImage(file="boss.png")
                        canvas.create_image(self.x, self.y, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)


mixer.init()
mixer.music.load('troi.mp3')
mixer.music.play(loops=-1, start= 0.0)


root = Tk()

canvas = Canvas(root, width='720', height='720')

background = Map()
background.draw_map()

angry_cloud = Angry_clouds()

for i in range(3):
    angry_cloud.angry_clouds_draw()

boss = Boss()
boss.boss_draw()
canvas.bind("<KeyPress>", boss.boss_move)

hero = Hero()
canvas.bind("<KeyPress>", hero.on_key_press)

canvas.pack()
canvas.focus_set()

root.mainloop()