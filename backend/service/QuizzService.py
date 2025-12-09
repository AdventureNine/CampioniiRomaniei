from backend.domain.entities.Quizz import Quizz
from backend.repository.QuizzRepository import QuizzRepository


class QuizzService:
    def __init__(self, repository: QuizzRepository):
        self._repository = repository

    def create_quizz(self, quizz_id: int, questions: list, fill_in_statements: list, minigames: list, difficulty: str, completion_percentage: float) -> Quizz:
        quizz = Quizz(quizz_id, questions, fill_in_statements, minigames, difficulty, completion_percentage)
        self._repository.add(quizz)
        return quizz

    def get_quizz(self, quizz_id: int) -> Quizz:
        return self._repository.get_by_id(quizz_id)

    def get_quizzes_by_difficulty(self, difficulty: str) -> list[Quizz]:
        return self._repository.find(f"difficulty = '{difficulty}'")

    def get_all_quizzes(self) -> list[Quizz]:
        return self._repository.get_all()

    def update_completion_percentage(self, quizz_id: int, percentage: float) -> Quizz:
        quizz = self._repository.get_by_id(quizz_id)
        if quizz:
            quizz.set_completion_percentage(percentage)
            self._repository.update(quizz)
            return quizz
        return None
