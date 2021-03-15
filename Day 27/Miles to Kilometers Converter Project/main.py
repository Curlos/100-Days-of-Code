from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)

# Labels
label_one = Label(text="is equal to", font=("Arial", 16))
label_one.grid(column=0, row=1)

label_two_km = Label(text="0", font=("Arial", 16))
label_two_km.grid(column=1, row=1)
label_two_km.config(padx=10)

label_three = Label(text="Km", font=("Arial", 16))
label_three.grid(column=2, row=1)

label_four = Label(text="miles", font=("Arial", 16))
label_four.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Button


def convert_mile_to_km():
    label_two_km["text"] = str(int(input.get()) * 1.609)


button = Button(text="Calculate", command=convert_mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
