from typing import Optional, List
from backend.repository.QuestionRepository import QuestionRepository
from backend.domain.entities.Question import Question


class QuestionService:
    def __init__(self, question_repository: QuestionRepository):
        self.question_repository = question_repository

    def create_question(self, question: Question) -> None:
        """Create and save a new question."""
        self.question_repository.save(question)

    def get_question_by_id(self, question_id: int) -> Optional[Question]:
        """Get a question by its ID."""
        return self.question_repository.get_by_id(question_id)

    def update_question(self, question: Question) -> None:
        """Update an existing question."""
        self.question_repository.save(question)

    def delete_question(self, question_id: int) -> None:
        """Delete a question by ID."""
        self.question_repository.delete_by_id(question_id)

    def find_questions(self, where_clause: str) -> List[Question]:
        """Find questions matching a where clause."""
        return self.question_repository.find(where_clause)

    def check_answer(self, question: Question, user_answers: List[str]) -> bool:
        """Check if the user's answers are correct."""
        return question.check_answers(user_answers)

    def get_correct_answers(self, question: Question) -> List[str]:
        """Get all correct answers for a question."""
        correct_answers = []
        for answer_text, is_correct in question.get_answer_data():
            if is_correct:
                correct_answers.append(answer_text)
        return correct_answers

    def get_all_answer_options(self, question: Question) -> List[str]:
        """Get all answer options (both correct and incorrect)."""
        return [answer_text for answer_text, _ in question.get_answer_data()]

    def is_multiple_choice(self, question: Question) -> bool:
        """Check if the question has multiple correct answers."""
        correct_count = sum(1 for _, is_correct in question.get_answer_data() if is_correct)
        return correct_count > 1

    def get_questions_by_quizz(self, quizz_id: int) -> List[Question]:
        """Get all questions for a specific quizz."""
        return self.question_repository.find(f"quizz = {quizz_id}")

    def validate_answer_count(self, question: Question) -> bool:
        """Validate that the question has at least one correct answer."""
        correct_count = sum(1 for _, is_correct in question.get_answer_data() if is_correct)
        return correct_count > 0
