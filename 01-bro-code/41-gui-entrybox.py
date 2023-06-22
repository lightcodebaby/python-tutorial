from tkinter import *

window = Tk()

entry = Entry(window, font=("Arial", 50), fg="#00FF00", bg="black", show="_")
entry.insert(0, "Text by default")
entry.pack(side=LEFT)


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, len(entry.get()))


def backspace():
    entry.delete(len(entry.get()) - 1), len(entry.get())


submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
