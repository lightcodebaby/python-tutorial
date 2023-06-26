from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_left(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_right(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

race_car = PhotoImage(file="./race-car.png")
label = Label(window, image=race_car, anchor=NW)
label.place(x=0, y=0)

window.mainloop()
