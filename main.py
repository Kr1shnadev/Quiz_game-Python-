from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]

for question in question_data:
    text = question["question"]
    ans= question["correct_answer"]
    new_question = Question(text,ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while(quiz.still_has_questions()):
    quiz.nextQuestion()
print("You've completed the quiz!!!!!!!!!!!!")
print(f"Your Final score is {quiz.score}/{len(question_bank)}")

