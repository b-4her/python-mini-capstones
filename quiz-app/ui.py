THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInteface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.score = 0
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Labels
        self.score_text = Label(text= f"Score = {self.score}", bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        #Buttons
        self.false_img = PhotoImage(file=r"images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, borderwidth=0,
                                command=self.false_check)
        self.false_btn.grid(column=1, row=2)
        
        self.true_img = PhotoImage(file=r"images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0, borderwidth=0,
                                command=self.true_check)
        self.true_btn.grid(column=0, row=2)
        
        #Canvas
        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.question_text = self.canvas.create_text((150,125), text="my question", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")
            self.canvas.configure(bg="white")
        
    def true_check(self):
        answer = self.quiz.check_answer("True")

        if answer:
            self.score += 1
            self.score_text.config(text= f"Score = {self.score}")
            self.canvas.configure(bg="green")
            
        else: 
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)   

        

    def false_check(self):
        answer = self.quiz.check_answer("False")

        if answer:
            self.score += 1
            self.score_text.config(text= f"Score = {self.score}")
            self.canvas.configure(bg="green")
        
        else: 
            self.canvas.configure(bg="red")
        
        self.window.after(1000, self.get_next_question) 
           

        

       

