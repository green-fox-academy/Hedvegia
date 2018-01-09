import game
from tkinter import *

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