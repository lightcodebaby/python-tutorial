from tkinter import *

window = Tk()

text_area = Text(
    window,
    bg="light yellow",
    font=("Ink Free", 25),
    height=8,
    width=20,
    padx=20,
    pady=20,
    fg="purple",
)


def submit():
    print(text_area.get("1.0", END))


submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

text_area.pack()

window.mainloop()
