from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question_num = 1

for question in question_data["results"]:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.print_final_score()
