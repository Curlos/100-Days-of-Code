from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

# Button


def button_clicked():
    my_label["text"] = input.get()


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=3)


window.mainloop()
