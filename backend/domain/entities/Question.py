from backend.domain.entities.QuizzTask import QuizzTask

class Question(QuizzTask):
    def __init__(self, question_id: int, text: str, answer_list: list[str]):
        super().__init__(question_id, answer_list)
        self.__text = text

    def get_text(self): return self.__text

    def __str__(self): return f"Question {self._id}. Text: {self.__text}. Answer(s): {self._answer_list} "