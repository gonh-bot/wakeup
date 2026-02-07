# main.py

from core.config import QUESTIONS
from core.quiz import QuizManager
from core.audio import play_alarm
from ui.screen import WakeUpScreen

def on_correct():
    play_alarm()

def on_finish():
    print("起床成功")

if __name__ == "__main__":
    quiz = QuizManager(QUESTIONS)
    screen = WakeUpScreen(
        quiz=quiz,
        on_correct=on_correct,
        on_finish=on_finish
    )
    screen.run()
