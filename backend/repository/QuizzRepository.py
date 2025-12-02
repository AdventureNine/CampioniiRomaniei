from typing import Optional, List, Callable, Any
from backend.domain.entities.Quizz import Quizz


class QuizzRepository:
    def __init__(self):
        self.__quizzes: dict[int, Quizz] = {}

    def save(self, quizz: Quizz) -> None:
        if not isinstance(quizz, Quizz):
            raise TypeError("Object must be of type Quizz.")

        quizz_id = quizz.get_id()
        self.__quizzes[quizz_id] = quizz

    def get_by_id(self, quizz_id: int) -> Optional[Quizz]:
        return self.__quizzes.get(quizz_id)

    def get_all(self) -> List[Quizz]:
        return list(self.__quizzes.values())

    def delete_by_id(self, quizz_id: int) -> None:
        if quizz_id in self.__quizzes:
            del self.__quizzes[quizz_id]
        else:
            raise KeyError(f"No Quizz exists with ID {quizz_id} for deletion.")

    def find(self, filter_func: Callable[[Quizz], bool]) -> List[Quizz]:
        results: List[Quizz] = []
        for quizz in self.__quizzes.values():
            if filter_func(quizz):
                results.append(quizz)
        return results