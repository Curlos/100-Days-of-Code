from tkinter import *
from tkinter import messagebox
from password_generator import Password
import pyperclip
import json

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password = Password()
    password = password.generate_password()

    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', mode="w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, 'end')
            password_input.delete(0, 'end')

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        with open('data.json', mode="r") as data_file:
            # Reading old data
            data = json.load(data_file)
            try:
                website_name = website_input.get()
                website = data[website_name]
                email = website["email"]
                password = website["password"]
                messagebox.showinfo(
                    title=f"{website_name}", message=f"Email: {email}\n" f"Password: {password}\n" f"Password copied to clipboard")
                pyperclip.copy(password)

            except KeyError:
                messagebox.showinfo(
                    title=f"{website_name}", message=f"No details for the website '{website_name}' exists.")
    except FileNotFoundError:
        messagebox.showinfo(
            title=f"{website_name}", message=f"No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text="Website:", font=(
    "Arial", 12))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=(
    "Arial", 12))
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(
    "Arial", 12))
password_label.grid(column=0, row=3)

# Entries

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, 'curlosmart@gmail.com')

password_input = Entry(width=21)
password_input.grid(row=3, column=1)


# Buttons
password_button = Button(text="Search", command=find_password, width=13)
password_button.grid(column=2, row=1)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

window.mainloop()
