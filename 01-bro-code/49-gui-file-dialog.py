from tkinter import *
from tkinter import filedialog

window = Tk()


def open_file():
    file_path = filedialog.askopenfilename(
        initialdir="./",
        title="Open file okay?",
        filetypes=(("text files", "*.txt"), ("csv files", "*.csv")),
    )
    print(file_path)


def save_file():
    file = filedialog.asksaveasfile(
        initialdir="./",
        defaultextension=".txt",
        filetypes=[("Text file", ".txt"), ("HTML file", ".html"), ("All files", ".*")],
    )
    file_text = str(text_area.get(1.0, END))
    file.write(file_text)
    file.close()


file_button = Button(text="Open", command=open_file)
file_button.pack()

save_button = Button(text="Save", command=save_file)
save_button.pack()

text_area = Text(window)
text_area.pack

window.mainloop()
