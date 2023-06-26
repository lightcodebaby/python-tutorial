import time
from tkinter import *
from tkinter.ttk import *


def start():
    tasks = 10
    done = 0
    while done < tasks:
        time.sleep(1)
        bar["value"] += 10
        done += 1
        percent.set(str(((done / tasks)) * 100))
        window.update()


window = Tk()

percent = StringVar()

bar = Progressbar(window, orient=HORIZONTAL)
bar.pack(pady=10)

percent_label = Label(window, textvariable=percent)
percent_label.pack()

button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()
