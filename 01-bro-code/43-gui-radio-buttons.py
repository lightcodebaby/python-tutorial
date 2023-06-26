from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

window = Tk()

x = IntVar()


def order():
    print("You ordered " + food[x.get()])


for index in range(len(food)):
    radio_button = Radiobutton(
        window,
        text=food[index],
        value=index,
        variable=x,
        padx=25,
        font=("Impact", 50),
        indicatoron=0,
        command=order,
    )
    radio_button.pack(anchor=W)

window.mainloop()
