import time
from tkinter import *

WIDTH = 500
HEIGHT = 500
X_VELOCITY = 1
Y_VELOCITY = 1

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

plane_image = PhotoImage(file="./plane.png")
my_image = canvas.create_image(0, 0, image=plane_image, anchor=NW)

image_width = plane_image.width()
image_height = plane_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    window.update()
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        X_VELOCITY *= -1
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        Y_VELOCITY *= -1
    canvas.move(my_image, X_VELOCITY, Y_VELOCITY)
    time.sleep(0.01)

window.mainloop()
