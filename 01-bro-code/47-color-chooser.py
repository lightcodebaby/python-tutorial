from tkinter import *
from tkinter import colorchooser

window = Tk()
window.geometry("420x420")

def click():
    window.config(bg=colorchooser.askcolor()[1])

button = Button(window, text="click me", command=click)
button.pack()


window.mainloop()