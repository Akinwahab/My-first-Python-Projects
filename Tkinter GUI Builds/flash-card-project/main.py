from tkinter import *
import pandas
import random
# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None
to_learn = {}


#---------------------------- FLASH CARD MECHANISM ------------------------------- #

try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/japanese_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

    
def next_card():
    global current_card, flip_timer
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="Japanese", fill="black")
    canvas.itemconfig(card_word, text=current_card["Japanese_English"], fill="black")
    if flip_timer:
        window.after_cancel(flip_timer)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#----------------------------UI SETUP ------------------------------- #
#window 
window = Tk()
window.title("AkinFlashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

#buttons
wrong_image = PhotoImage(file="images/wrong.png")
miss_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
miss_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
get_button = Button(image=right_image, highlightthickness=0, command=is_known)
get_button.grid(row=1, column=1)

next_card()
window.mainloop()

