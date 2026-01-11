class QuizzTask:
    def __init__(self, task_id: int, answer_list: list[str]):
        self._id = task_id
        self._answer_list = answer_list

    def get_id(self): return self._id
    def get_answer_list(self): return self._answer_list
    def check_answers(self, answers: list[str]):
        for answer in answers:
            if answer not in self._answer_list: return False
        return True