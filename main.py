import data
from question_model import Question
from quiz_brain import QuizBrain

print("Starting Quiz, Please answer the following Questions")
totalscore = 0
counter=1
for x in data.question_data["results"]:
    question = Question(x.get("question"), x.get("correct_answer"))
    quiz_brain = QuizBrain()
    user_answer = input(f"Q{counter}: {question.text}(True/False)")
    quiz_brain.check_answer(question.answer,user_answer )
    totalscore += quiz_brain.score
    counter += 1

print("Quiz finished")
print(f"Your total score is: {totalscore}")
