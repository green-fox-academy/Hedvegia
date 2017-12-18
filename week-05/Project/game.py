from tkinter import *

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()


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
                    image = canvas.create_image(x+j*72, y+i*72, image=self.tile)
                else:
                    image = canvas.create_image(x+j*72, y+i*72, image=self.wall)

background = Map()
background.background_tiles(36, 36)


root.mainloop()