from typing import Optional, List, Callable, Any
from backend.domain.entities.QuizzTask import QuizzTask


class QuizzTaskRepository:
    def __init__(self):
        self.__tasks: dict[int, QuizzTask] = {}

    def save(self, task: QuizzTask) -> None:
        if not isinstance(task, QuizzTask):
            raise TypeError("Object must be of type QuizzTask or a subclass thereof.")

        task_id = task._id
        self.__tasks[task_id] = task

    def get_by_id(self, task_id: int) -> Optional[QuizzTask]:
        return self.__tasks.get(task_id)

    def get_all(self) -> List[QuizzTask]:
        return list(self.__tasks.values())

    def delete_by_id(self, task_id: int) -> None:
        if task_id in self.__tasks:
            del self.__tasks[task_id]
        else:
            raise KeyError(f"No QuizzTask exists with ID {task_id} for deletion.")

    def find(self, filter_func: Callable[[QuizzTask], bool]) -> List[QuizzTask]:
        results: List[QuizzTask] = []
        for task in self.__tasks.values():
            if filter_func(task):
                results.append(task)
        return results