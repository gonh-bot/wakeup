import tkinter as tk
import os
class WakeUpScreen:
    def __init__(self, quiz, on_correct, on_finish):
        self.quiz = quiz
        self.on_correct = on_correct
        self.on_finish = on_finish

        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)

        self.left = tk.Frame(self.root, bg="white")
        self.right = tk.Frame(self.root, bg="black")

        self.left.pack(side="left", fill="both", expand=True)
        self.right.pack(side="right", fill="both", expand=True)

        self.question_label = tk.Label(
            self.root,
            text=self.quiz.current_question(),
            font=("Arial", 36),
            bg="gray"
        )
        self.question_label.place(relx=0.5, rely=0.2, anchor="center")

        self.feedback = tk.Label(
            self.root,
            text="",
            font=("Arial", 24),
            bg="gray"
        )
        self.feedback.place(relx=0.5, rely=0.3, anchor="center")

        tk.Button(
            self.left,
            text="YES",
            font=("Arial", 40),
            command=lambda: self.answer("yes")
        ).place(relx=0.5, rely=0.6, anchor="center")

        tk.Button(
            self.right,
            text="NO",
            font=("Arial", 40),
            command=lambda: self.answer("no")
        ).place(relx=0.5, rely=0.6, anchor="center")

    def answer(self, choice):
        if self.quiz.check_answer(choice):
            self.feedback.config(text="✔ 正确", fg="green")
            self.on_correct()

            if self.quiz.finished():
                self.on_finish()
                self.root.after(1500, self.root.destroy)
            else:
                self.question_label.config(
                    text=self.quiz.current_question()
                )
        else:
            self.feedback.config(text="✘ 错误", fg="red")

    def run(self):
        self.root.mainloop()
    os.startfile(r"D:\\osulazer\\current\\osu!.exe")