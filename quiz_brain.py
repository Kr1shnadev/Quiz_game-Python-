class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def nextQuestion(self):
        current = self.question_list[self.question_number]
        user_input=input(f"Q.{self.question_number+1}: {current.question}(True/False) ?:")
        self.question_number +=1
        self.check_answer(current.answer,user_input)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    def check_answer(self,correct_ans,user_ans):
        if (user_ans.lower()==correct_ans.lower()):
            self.score+=1
            print("That's correct")
        else:
            print(f"Thats wrong.")
        print(f"The correct answer is {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
