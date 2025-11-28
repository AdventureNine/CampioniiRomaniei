from backend.domain.entities.QuizzTask import QuizzTask

class FillInStatement(QuizzTask):
    def __init__(self, fill_in_id: int, text_segments: list[str], answer_list: list[str]):
        super().__init__(fill_in_id, answer_list)
        self.__text_segments = text_segments

    def get_text_segments(self): return self.__text_segments

    def __str__(self): return f"Fill-in statement {self._id}. Text: {self.__text_segments}. Answers: {self._answer_list} "