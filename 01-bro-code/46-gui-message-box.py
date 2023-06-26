from tkinter import *
from tkinter import messagebox

window = Tk()


def click():
    messagebox.showinfo(title="My first info message box", message="Hello World")
    messagebox.showwarning(title="My first warning message box", message="Hello World")
    messagebox.showerror(title="My first error message box", message="Hello World")

    if messagebox.askokcancel(
        title="ask ok cancel", message="Ok or cancel?", icon="warning"
    ):
        print("Ok")
    else:
        print("Cancel")

    if messagebox.askretrycancel(
        title="ask retry cancel", message="Retry or cancel?", icon="error"
    ):
        print("Retry")
    else:
        print("Cancel")

    if messagebox.askyesno(title="ask yes no", message="Yes or no?", icon="info"):
        print("Yes")
    else:
        print("No")

    answer = messagebox.askquestion(
        title="ask question", message="Can you answer this question?"
    )
    print(answer)

    answer = messagebox.askyesnocancel(
        title="ask yes no cancel", message="Yes, no or cancel?"
    )
    print(answer)


button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()
