from tkinter import *


def move_up(event):
    canvas.move(race_car_image, 0, -10)


def move_left(event):
    canvas.move(race_car_image, -10, 0)


def move_down(event):
    canvas.move(race_car_image, 0, 10)


def move_right(event):
    canvas.move(race_car_image, 10, 0)


window = Tk()

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)


race_car = PhotoImage(file="./race-car.png")

canvas = Canvas(window, width=500, height=500)
canvas.image = race_car
canvas.pack()
race_car_image = canvas.create_image(0, 0, image=race_car, anchor=NW)

window.mainloop()
