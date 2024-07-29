from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizzInterface

# getting the data from API
parameter = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=parameter)
response.raise_for_status()
response_json = response.json()
question_data = response_json["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
ui_interface = QuizzInterface(quiz)
