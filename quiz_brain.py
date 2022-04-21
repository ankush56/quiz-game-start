class QuizBrain:
    def __init__(self):
        self.score = 0

    def check_answer(self, answer, user_answer):
        if answer == user_answer:
            self.score = self.score + 1
            print("Answer is correct")
        else:
            print("Incorrect Answer")
