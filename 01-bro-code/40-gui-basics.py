from tkinter import *

window = Tk()
# window.geometry("420x420")
window.title("My First Python GUI")

# config
icon = PhotoImage(file="./01-bro-code/python-logo.png")
window.iconphoto(True, icon)
window.config(background="black")  # or hex values

# photos
photo = PhotoImage(file="./01-bro-code/python-logo.png")

# labels
label = Label(
    window,
    text="Hello World",
    font=("Arial", 40, "bold"),
    fg="#00FF00",
    bg="black",
    relief=RAISED,
    bd=10,
    padx=20,
    pady=20,
    #    image=photo,
    compound="top",
)
label.pack()  # center


# buttons
def click():
    print("You clicked the button!")


button = Button(
    window,
    text="Click me!",
    command=click,
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    state=ACTIVE,
    image=photo,
    compound="bottom",
)
button.pack()

# label2 = Label(window, text="My second label")
# label.place(x=0, y=0)

window.mainloop()
