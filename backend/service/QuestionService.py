from backend.domain.entities.Question import Question
from backend.repository.QuestionRepository import QuestionRepository


class QuestionService:
    def __init__(self, repository: QuestionRepository):
        self._repository = repository

    def create_question(self, question_id: int, quizz_id: int, text: str, answer_list: list[str]) -> Question:
        question = Question(question_id, text, answer_list)
        self._repository.add(question, quizz_id)
        return question

    def get_question(self, question_id: int) -> Question:
        return self._repository.get_by_id(question_id)

    def get_questions_by_quizz(self, quizz_id: int) -> list[Question]:
        return self._repository.get_all(quizz_id)

    def update_question(self, question_id: int, new_text: str, new_answer_list: list[str]) -> Question:
        question = self._repository.get_by_id(question_id)
        if question:
            # Note: The Question entity does not have setters for text or answer_list directly
            # This would require modifying the Question entity or recreating it.
            # For now, I'll just update the text and assume a new object if answer list changes.
            updated_question = Question(question_id, new_text, new_answer_list)
            self._repository.update(updated_question)
            return updated_question
        return None

    def delete_question(self, question_id: int):
        self._repository.delete(question_id)
