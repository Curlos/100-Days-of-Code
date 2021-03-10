class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def printQuestion(self):
        print(f"Question: {self.text} Answer: {self.answer}")
