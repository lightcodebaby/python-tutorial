from tkinter import *

window = Tk()

first_name_label = Label(window, text="First name")
first_name_entry = Entry(window)

first_name_label.grid(row=0, column=0)
first_name_entry.grid(row=0, column=1)

last_name_label = Label(window, text="Last name")
last_name_entry = Entry(window)

last_name_label.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

email_label = Label(window, text="Email")
email_entry = Entry(window)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)

submit_button = Button(window, text="Submit")
submit_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
