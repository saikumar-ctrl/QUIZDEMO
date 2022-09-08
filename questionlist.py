class quiz:
    def __init__(self,question):
        self.question_no=0
        self.question=question
        self.score=0
    def Nextquestion(self):
        quiz_question=self.question[self.question_no].question
        ans=input(f"Q{self.question_no+1}: {quiz_question}:(True/False) ")
        self.question_no += 1
        if ans==self.question[self.question_no-1].answer:
            self.score+=1
            print(f"your score is {self.score}/{self.question_no}")
        else:
            print(f"your score is {self.score}/{self.question_no}")
        if self.question_no!=len(self.question):
            self.Nextquestion()


