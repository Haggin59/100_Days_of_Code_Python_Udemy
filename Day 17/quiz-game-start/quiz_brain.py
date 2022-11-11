class QuizBrain:
    def __init__(self, q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(current_question.text)
        self.check_answer(user_ans,current_question.answer)


    def still_has_qns(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer , correct_answer):
        if user_answer == correct_answer:
            print("Answer is correct")
            self.score += 1

        else:
            print("Answer is not correct")
        print(f"Correct Answer: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        

    
        

