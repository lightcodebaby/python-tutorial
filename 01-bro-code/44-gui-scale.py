from tkinter import *

window = Tk()

scale = Scale(
    window,
    from_=100,
    to=0,
    length=600,
    orient=VERTICAL,
    font=("Consolas", 20),
    tickinterval=10,
    showvalue=1,
    resolution=5,
    troughcolor="#69EAFF",
    fg="#FF1C00",
    bg="#111111",
)
scale.set(((scale["from"] - scale["to"]) / 2) + scale["to"])
scale.pack()


def submit():
    print("The temperature is: " + str(scale.get()) + "ºC")


button = Button(
    window,
    text="submit",
    command=submit,
)
button.pack()

window.mainloop()
