from tkinter import Tk, Label, Button, Entry, Radiobutton, IntVar
from converter import Converter

UNITS = ["Kilometers", "Meters", "Centimeters", "Millimeters", "Micrometers",
         "Nanometers", "Miles", "Yards", "Feet", "Inches", "Nautical Miles"]

val = 0
final_unit = 'kilometers'
labels = []

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)

# Labels

for i, unit_name in enumerate(UNITS):
    unit = Label(text=f"0 {unit_name}", font=("Arial", 16))
    unit.grid(column=1, row=i)
    unit.config(padx=10)
    labels.append(unit)


# Radiobutton
def change_unit():
    final_unit = UNITS[radio_state.get()].lower()


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()

for i, unit_name in enumerate(UNITS):
    unit = Radiobutton(text=f"{unit_name}", value=i,
                       variable=radio_state, command=change_unit)
    unit.grid(column=0, row=i)
    unit.config(padx=10)

# Entry
input = Entry(width=10)
input.grid(column=0, row=13)

# Button
def convert_to_all_units():
    val = float(input.get())
    c = Converter(val, final_unit)
    conversions = c.convert()

    for i, label in enumerate(labels):
        current_unit_name = UNITS[i]
        label["text"] = f"{conversions.get(current_unit_name.lower())} {current_unit_name}"


button = Button(text="Calculate", command=convert_to_all_units)
button.grid(column=1, row=13)

window.mainloop()
