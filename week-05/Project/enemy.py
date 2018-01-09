import game
from tkinter import *
from hero import Hero
import random


class Enemies(object):
    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    class Angry_clouds(Enemies):
        def __init__(self, x, y):
            super().__init__(x, y)
            self.angry_clouds = PhotoImage(file='angry_clouds.png')

        def angry_clouds_draw(self):
            self.x = random.randrange(72, 576, 72)
            self.y = random.randrange(0, 576, 72)
            if background.wall_or_tile[self.y//72][self.x//72] == 0:
                canvas.create_image(self.x, self.y, anchor=NW, image=self.angry_clouds)
            else:
                return self.angry_clouds_draw()
            self.angry_clouds_move

        def angry_clouds_move(self, e):
            if e.keysym == "Right" or e.keysym == "Left" or e.keysym == "Up" or e.keysym == "Down":

                t = random.randint(1, 5)

                if t == 1:
                    if self.x <= 576 and background.wall_or_tile[(self.y)//72][(self.x+72)//72] == 0:
                        canvas.create_image(self.x + 72, self.y, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)

                elif t == 2:
                    if self.x >= 72 and background.wall_or_tile[(self.y)//72][(self.x-72)//72] == 0:
                        canvas.create_image(self.x-72, self.y, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)

                elif t == 3:
                    if self.y <= 576 and background.wall_or_tile[(self.y+72)//72][(self.x)//72] == 0:
                        canvas.create_image(self.x, self.y + 72, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)

                elif t == 3:
                    if self.y >= 72 and background.wall_or_tile[(self.y-72)//72][(self.x)//72] == 0:
                        canvas.create_image(self.x, self.y - 72, anchor=NW, image=self.angry_clouds)
                    else:
                        return self.angry_clouds_move(e)


    class Boss(object):
        def __init__(self):
            super().__init__(x, y)
            self.boss = PhotoImage(file="boss.png")


        def boss_draw(self):
            self.x = random.randrange(144, 576, 72)
            self.y = random.randrange(144, 576, 72)
            if background.wall_or_tile[self.y//72][self.x//72] == 0:
                canvas.create_image(self.x, self.y, anchor=NW, image=self.boss)
            else:
                return self.boss_draw()
            self.boss_move
                
        def boss_move(self, e):
            if e.keysym == "Right" or e.keysym == "Left" or e.keysym == "Up" or e.keysym == "Down":

                t = random.randint(1, 5)

                if t == 1:
                    if self.x <= 576 and background.wall_or_tile[(self.y)//72][(self.x+72)//72] == 0:
                        canvas.create_image(self.x + 72, self.y, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)

                elif t == 2:
                    if self.x >= 72 and background.wall_or_tile[(self.y)//72][(self.x-72)//72] == 0:
                        canvas.create_image(self.x-72, self.y, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)

                elif t == 3:
                    if self.y <= 576 and background.wall_or_tile[(self.y+72)//72][(self.x)//72] == 0:
                        canvas.create_image(self.x, self.y + 72, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)

                elif t == 3:
                    if self.y >= 72 and background.wall_or_tile[(self.y-72)//72][(self.x)//72] == 0:
                        canvas.create_image(self.x, self.y - 72, anchor=NW, image=self.boss)
                    else:
                        return self.boss_move(e)