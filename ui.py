from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        windows = Tk()
        windows.title("Quizz Game")
        windows.config(bg=THEME_COLOR, pady=20, padx=20)
        # creating the canvas
        self.canvas = Canvas()
        self.canvas.config(height=250, width=300)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=200,
                                                     text="",
                                                     font=("Ariel", 18, "italic"), )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # creating the buttons
        # wrong btn
        w_btn_pic = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(width=100, height=97, image=w_btn_pic, highlightthickness=0, command=self.wrong_button)
        self.wrong_btn.grid(column=0, row=2)
        # right btn
        r_btn_pic = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=r_btn_pic, height=97, width=100, highlightthickness=0,
                                command=self.correct_btn,
                                )
        self.right_btn.grid(row=2, column=1)
        # the score holder
        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="#ffffff")
        self.score.grid(row=0, column=1)
        self.get_next_question()

        windows.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reach the end of the questions!")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def correct_btn(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(is_true)

    def wrong_button(self):
        is_true = self.quiz.check_answer("False")
        self.give_feedback(is_true)

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.reset)

    def reset(self):
        self.canvas.config(bg="white")
        self.get_next_question()
