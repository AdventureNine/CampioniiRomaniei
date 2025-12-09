from backend.dtos.QuestionDTO import QuestionDTO

class QuizDataDTO:
    def __init__(self, questions: list[QuestionDTO], timer: int):
        self.questions = questions
        self.timer = timer
