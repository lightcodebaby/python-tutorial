from tkinter import *


def do_something_with_keyboard(event):
    label.config(text=event.keysym)


def do_something_with_mouse(event):
    print("Mouse coordinates: " + str(event.x) + ", " + str(event.y))


window = Tk()

window.bind("<Key>", do_something_with_keyboard)
window.bind("<Button-1>", do_something_with_mouse)
window.bind("<Button-2>", do_something_with_mouse)
window.bind("<Button-3>", do_something_with_mouse)
window.bind("<ButtonRelease>", do_something_with_mouse)
window.bind("<Enter>", do_something_with_mouse)
window.bind("<Leave>", do_something_with_mouse)
window.bind("<Motion>", do_something_with_mouse)

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
