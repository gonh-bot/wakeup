class QuizManager:
    def __init__(self, questions):
        self.questions = questions
        self.index = 0

    def current_question(self):
        return self.questions[self.index]["question"]

    def check_answer(self, choice):
        correct = self.questions[self.index]["answer"]
        if choice == correct:
            self.index += 1
            return True
        return False

    def finished(self):
        return self.index >= len(self.questions)