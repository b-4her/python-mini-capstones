from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 35
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timing = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timing)
    canvas.itemconfig(timer, text="00:00")
    title_txt.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        title_txt.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title_txt.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_txt.config(text="Break", fg=PINK)
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    minutes = floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer, text=f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
    if count > 0:
        global timing
        timing = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            work_sessions = (reps+1)/2
            check_mark.config(text= "✔" * int(work_sessions))
        reps += 1
        window.after(1000, start_timer)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50 ,bg=YELLOW) 

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00" ,fill="white", 
                           font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Labels
title_txt = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50),
                   bg=YELLOW, highlightthickness=0)
title_txt.grid(row=0, column=1)

start_btn = Button(borderwidth=0, text="Start", bg="white",
                    highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(borderwidth=0, text="Reset", bg="white",
                    highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2, column=2)

check_mark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0,
                    font=(FONT_NAME, 15))
check_mark.grid(column=1, row=3)





window.mainloop()

