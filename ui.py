import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT_SMALL = ("Arial", 12, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Window setup
        self.window = tk.Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Canvas setup
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="",
            font=FONT,
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        # Label setup
        self.score_label = tk.Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=FONT_SMALL)
        self.score_label.grid(column=1, row=0)

        # Button setup
        true_img = tk.PhotoImage(file="./images/true.png")
        false_img = tk.PhotoImage(file="./images/false.png")
        self.true_button = tk.Button(image=true_img,
                                     highlightthickness=0,
                                     command=self.true_pressed
                                     )
        self.false_button = tk.Button(image=false_img,
                                      highlightthickness=0,
                                      command=self.false_pressed
                                      )
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"

    def true_pressed(self):
        self.check_answer(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.check_answer(self.quiz.check_answer("False"))

    def check_answer(self, correct: bool):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
