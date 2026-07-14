from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280, 
            text="Testing",
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")  
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right)
        self.right_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png",)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\n Final Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)