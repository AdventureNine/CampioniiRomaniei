from typing import Optional, List
from backend.repository.QuizzTaskRepository import QuizzTaskRepository


class QuizzTaskService:
    def __init__(self, quizz_task_repository: QuizzTaskRepository):
        self.quizz_task_repository = quizz_task_repository

    def get_task_by_id(self, task_id: int) -> Optional[dict]:
        """Get a quizz task by its ID."""
        return self.quizz_task_repository.get_by_id(task_id)

    def get_all_tasks(self) -> List[dict]:
        """Get all quizz tasks."""
        return self.quizz_task_repository.get_all()

    def delete_task(self, task_id: int) -> None:
        """Delete a quizz task by ID."""
        self.quizz_task_repository.delete_by_id(task_id)

    def find_tasks(self, where_clause: str) -> List[dict]:
        """Find tasks matching a where clause."""
        return self.quizz_task_repository.find(where_clause)

    def get_tasks_by_type(self, task_type: str) -> List[dict]:
        """Get all tasks of a specific type."""
        return self.quizz_task_repository.find(f"type = '{task_type}'")

    def get_tasks_by_quizz(self, quizz_id: int) -> List[dict]:
        """Get all tasks for a specific quizz."""
        return self.quizz_task_repository.find(f"quizz = {quizz_id}")

    def count_tasks_by_type(self, task_type: str) -> int:
        """Count the number of tasks of a specific type."""
        tasks = self.get_tasks_by_type(task_type)
        return len(tasks)

    def count_tasks_in_quizz(self, quizz_id: int) -> int:
        """Count the total number of tasks in a quizz."""
        tasks = self.get_tasks_by_quizz(quizz_id)
        return len(tasks)

    def get_task_type(self, task_id: int) -> Optional[str]:
        """Get the type of a specific task."""
        task = self.quizz_task_repository.get_by_id(task_id)
        if task:
            return task.get("type")
        return None

    def validate_task_exists(self, task_id: int) -> bool:
        """Check if a task exists."""
        task = self.quizz_task_repository.get_by_id(task_id)
        return task is not None

    def get_task_statistics(self) -> dict:
        """Get statistics about all tasks in the system."""
        all_tasks = self.get_all_tasks()
        
        stats = {
            "total_tasks": len(all_tasks),
            "questions": 0,
            "fill_ins": 0,
            "other": 0
        }
        
        for task in all_tasks:
            task_type = task.get("type", "other")
            if task_type == "question":
                stats["questions"] += 1
            elif task_type == "fill-ins":
                stats["fill_ins"] += 1
            else:
                stats["other"] += 1
        
        return stats
