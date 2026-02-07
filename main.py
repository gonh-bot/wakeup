import time
import schedule

from core.config import QUESTIONS
from core.quiz import QuizManager
from core.audio import play_alarm
from ui.screen import WakeUpScreen

def my_job():
    def on_correct():
        play_alarm()

    def on_finish():
        print("起床成功")
 
    quiz = QuizManager(QUESTIONS)
    screen = WakeUpScreen(quiz=quiz,
                          on_correct=on_correct,
                          on_finish=on_finish)
    screen.run()

if __name__ == "__main__":
    schedule.every().day.at("07:00").do(my_job)
    while True:
        schedule.run_pending()
        time.sleep(1)