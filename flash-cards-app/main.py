from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# ------------------ words ----------------------
try:
    data = pandas.read_csv(r"data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"data/french_words.csv")
    word_list = data.to_dict(orient="records")
else: 
    word_list = data.to_dict(orient="records")

word = ""

def start():
    global word
    word = choice(word_list)
    flipcard()

def remembered(): # you have to delete the word from the list
    global flip_timer
    global word
    window.after_cancel(flip_timer)
    word_list.remove(word)
    data = pandas.DataFrame(word_list)
    data.to_csv(r"data/words_to_learn.csv", index=False)
    word = choice(word_list)
    flipcard()
    flip_timer = window.after(3000, backside)
    

def forgoted(): # you wont have to delete the word from the list
    global flip_timer
    global word
    window.after_cancel(flip_timer)
    word = choice(word_list)
    flipcard()
    flip_timer = window.after(3000, backside)


def flipcard():
    global word
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(written_word, text=word["French"])
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(language, fill="black")
    canvas.itemconfig(written_word, fill="black")
    

def backside():
    global word
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(written_word, text=word["English"])
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(language, fill="white")
    canvas.itemconfig(written_word, fill="white")

    
# ------------------------ UI -----------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_img = PhotoImage(file=r"images/card_front.png")
back_img = PhotoImage(file=r"images/card_back.png")

right_img = PhotoImage(file=r"images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, command=remembered)
right_btn.grid(column=1, row=1)

wrong_img = PhotoImage(file=r"images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=forgoted)
wrong_btn.grid(column=0, row=1)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image((400,263), image=front_img)
language = canvas.create_text((400,150), text="", font=("Arial",40,"italic"))
written_word = canvas.create_text((400,263), text="", font=("Arial",60,"bold"))
canvas.grid(columnspan=2, column=0,row=0)

start()
flip_timer = window.after(3000,backside)
window.mainloop()