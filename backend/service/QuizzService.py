from typing import Optional, List
from backend.repository.QuizzRepository import QuizzRepository
from backend.domain.entities.Quizz import Quizz


class QuizzService:
    def __init__(self, quizz_repository: QuizzRepository):
        self.quizz_repository = quizz_repository

    def create_quizz(self, quizz: Quizz) -> None:
        """Create and save a new quizz."""
        self.quizz_repository.save(quizz)

    def get_quizz_by_id(self, quizz_id: int) -> Optional[Quizz]:
        """Get a quizz by its ID."""
        return self.quizz_repository.get_by_id(quizz_id)

    def update_quizz(self, quizz: Quizz) -> None:
        """Update an existing quizz."""
        self.quizz_repository.save(quizz)

    def delete_quizz(self, quizz_id: int) -> None:
        """Delete a quizz by ID."""
        self.quizz_repository.delete_by_id(quizz_id)

    def find_quizzes(self, where_clause: str) -> List[Quizz]:
        """Find quizzes matching a where clause."""
        return self.quizz_repository.find(where_clause)

    def update_completion_percentage(self, quizz: Quizz, percentage: float) -> None:
        """Update the completion percentage of a quizz."""
        quizz.set_completion_percentage(percentage)
        self.quizz_repository.save(quizz)

    def get_quizzes_by_difficulty(self, difficulty: str) -> List[Quizz]:
        """Get all quizzes with a specific difficulty level."""
        return self.quizz_repository.find(f"difficulty = '{difficulty}'")

    def calculate_completion_percentage(self, quizz: Quizz, completed_tasks: int) -> float:
        """Calculate completion percentage based on completed tasks."""
        total_tasks = (len(quizz.get_questions()) + 
                      len(quizz.get_fill_in_statements()) + 
                      len(quizz.get_minigames()))
        
        if total_tasks == 0:
            return 0.0
        
        percentage = (completed_tasks / total_tasks) * 100
        return round(percentage, 2)

    def is_quizz_completed(self, quizz: Quizz) -> bool:
        """Check if a quizz is fully completed."""
        return quizz.get_completion_percentage() >= 100.0

    def get_total_tasks_count(self, quizz: Quizz) -> int:
        """Get the total number of tasks in a quizz."""
        return (len(quizz.get_questions()) + 
                len(quizz.get_fill_in_statements()) + 
                len(quizz.get_minigames()))
