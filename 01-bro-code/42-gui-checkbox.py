from tkinter import *

window = Tk()

x = BooleanVar()

python_logo = PhotoImage(file="./01-bro-code/python-logo.png")


def display():
    if x.get():
        print("You agree")
    else:
        print("You don't agree")


check_button = Checkbutton(
    window,
    text="I agree to something",
    variable=x,
    onvalue=True,
    offvalue=False,
    command=display,
    font=("Arial, 20"),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    padx=25,
    pady=10,
    image=python_logo,
    compound="left",
)
check_button.pack()

window.mainloop()
