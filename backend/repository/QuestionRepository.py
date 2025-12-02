from typing import Optional, List, Callable, Any
from backend.domain.entities.Question import Question


class QuestionRepository:
    def __init__(self):
        self.__questions: dict[int, Question] = {}

    def save(self, question: Question) -> None:
        if not isinstance(question, Question):
            raise TypeError("Object must be of type Question.")

        question_id = question._id
        self.__questions[question_id] = question

    def get_by_id(self, question_id: int) -> Optional[Question]:
        return self.__questions.get(question_id)

    def get_all(self) -> List[Question]:
        return list(self.__questions.values())

    def delete_by_id(self, question_id: int) -> None:
        if question_id in self.__questions:
            del self.__questions[question_id]
        else:
            raise KeyError(f"No Question exists with ID {question_id} for deletion.")

    def find(self, filter_func: Callable[[Question], bool]) -> List[Question]:
        results: List[Question] = []
        for question in self.__questions.values():
            if filter_func(question):
                results.append(question)
        return results