from tkinter import *
import json
import pandas
import random

df = pandas.read_csv("data/french_words.csv")
translations = {row.French: row.English for (index, row) in df.iterrows()}
french_words = list(translations.keys())
current_word = ''
card_flip = None

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)


def next_card():
    global current_word, flip_timer

    if current_word != '':
        print(translations.get(current_word))
        translations.pop(current_word)
        french_words.remove(current_word)
        print(translations.get(current_word))

    window.after_cancel(flip_timer)
    current_word = random.choice(french_words)
    english_translation = translations[current_word]

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(
        card_word, text=f"{current_word}", fill="black")
    canvas.itemconfig(card_img, image=card_front_img)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_word
    english_translation = translations[current_word]

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(
        card_word, text=f"{english_translation}", fill="white")
    canvas.itemconfig(
        card_img, image=card_back_img)


# Labels
card_title = canvas.create_text(400, 150, text="", fill="black",
                                font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text="", fill="black",
                               font=("Ariel", 60, "bold"))

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, bg=BACKGROUND_COLOR,
                      highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(
    image=right_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)
flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
