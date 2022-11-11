from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"],q["answer"]))

#print(question_bank[10].answer)

quiz = QuizBrain(question_bank)
quiz.next_question()
print("\n")


while quiz.still_has_qns():
    quiz.next_question()
    print("\n")

print(f"Quiz Finished, Your Score: {quiz.score}/{len(question_bank)}")