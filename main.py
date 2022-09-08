from questionmode import model
from data import question_data
from questionlist import quiz
questionbank=[]
for i in question_data:
    question_text=i['text']
    question_answer=i['answer']
    question=model(question_text,question_answer)
    questionbank.append(question)
brain=quiz(questionbank)
brain.Nextquestion()