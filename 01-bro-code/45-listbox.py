from tkinter import *

window = Tk()

list_box = Listbox(
    window, bg="#f7ffde", font=("Constantia", 35), width=12, selectmode=MULTIPLE
)
list_box.pack()

list_box.insert(1, "pizza")
list_box.insert(2, "pasta")
list_box.insert(3, "garlic bread")
list_box.insert(4, "soup")
list_box.insert(5, "salad")

list_box.config(height=list_box.size())

entry_box = Entry(window)
entry_box.pack()


def add():
    list_box.insert(list_box.size(), entry_box.get())
    list_box.config(height=list_box.size())


add_button = Button(window, text="add", command=add)
add_button.pack()


def delete():
    for index in reversed(list_box.curselection()):
        list_box.delete(index)
    list_box.config(height=list_box.size())


delete_button = Button(window, text="delete", command=delete)
delete_button.pack()


def submit():
    for index in list_box.curselection():
        print(list_box.get(index))


submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

window.mainloop()
