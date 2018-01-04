from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
first_list = [[10, 10], [290,  10], [290, 290], [10, 290]]
second_list =  [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
def draw(lst):
    lines = canvas.create_line(lst[0], lst[1], fill='green')
    lines = canvas.create_line(lst[1], lst[2], fill='green')
    lines = canvas.create_line(lst[2], lst[3], fill='green')
    lines = canvas.create_line(lst[3], lst[0], fill='green')
draw(first_list)
def draw_second(lst):
    lines = canvas.create_line(lst[0], lst[1], fill='green')
    lines = canvas.create_line(lst[1], lst[2], fill='green')
    lines = canvas.create_line(lst[2], lst[3], fill='green')
    lines = canvas.create_line(lst[3], lst[4], fill='green')
    lines = canvas.create_line(lst[4], lst[5], fill='green')
    lines = canvas.create_line(lst[5], lst[6], fill='green')
    lines = canvas.create_line(lst[6], lst[7], fill='green')
draw_second(second_list)
root.mainloop()