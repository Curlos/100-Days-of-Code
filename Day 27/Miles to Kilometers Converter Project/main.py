from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

# Labels

km = Label(text="0 kilometers", font=("Arial", 16))
km.grid(column=0, row=1)
km.config(padx=10)

cm = Label(text="0 centimeters", font=("Arial", 16))
cm.grid(column=0, row=2)
cm.config(padx=10)

mm = Label(text="0 milimeters", font=("Arial", 16))
mm.grid(column=0, row=3)
mm.config(padx=10)

miles = Label(text="0 miles", font=("Arial", 16))
miles.grid(column=0, row=4)
miles.config(padx=10)

yards = Label(text="0 Km", font=("Arial", 16))
yards.grid(column=0, row=5)
yards.config(padx=10)

inches = Label(text="0 Km", font=("Arial", 16))
inches.grid(column=0, row=6)
inches.config(padx=10)

feet = Label(text="0 Km", font=("Arial", 16))
feet.grid(column=0, row=7)
feet.config(padx=10)

# Entry
input = Entry(width=10)
input.grid(column=0, row=0)

# Checkbutton


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Button


def convert_mile_to_others():
    km["text"] = str(int(input.get()) * 1.609)


button = Button(text="Calculate", command=convert_mile_to_others)
button.grid(column=1, row=8)

window.mainloop()
