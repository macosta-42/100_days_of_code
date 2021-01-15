from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = ""
to_learn = {}

# ---------------------------- WORDS GENERATOR ------------------------------- #

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = {row.French: row.English for (index, row) in original_data.iterrows()}
except pandas.errors.EmptyDataError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = {row.French: row.English for (index, row) in original_data.iterrows()}
else:
    to_learn = {row.French: row.English for (index, row) in data.iterrows()}


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=to_learn[current_word], fill="white")


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(list(to_learn.keys()))
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word, fill="black")
    flip_timer = window.after(10000, flip_card)


def is_known():
    del to_learn[current_word]
    data = pandas.DataFrame(to_learn.items())
    data.to_csv("data/words_to_learn.csv", header=['French', 'English'], index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(10000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
