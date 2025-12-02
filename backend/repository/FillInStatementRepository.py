from typing import Optional, List, Callable, Any
from backend.domain.entities.FillInStatement import FillInStatement


class FillInStatementRepository:
    def __init__(self):
        self.__statements: dict[int, FillInStatement] = {}
        print("Repository In-Memory initialized.")

    def save(self, statement: FillInStatement) -> None:
        if not isinstance(statement, FillInStatement):
            raise TypeError("Object must be of type FillInStatement.")

        self.__statements[statement._id] = statement
        print(f"FillInStatement with ID {statement._id} has been saved/updated.")

    def get_by_id(self, fill_in_id: int) -> Optional[FillInStatement]:
        return self.__statements.get(fill_in_id)

    def get_all(self) -> List[FillInStatement]:
        return list(self.__statements.values())

    def delete_by_id(self, fill_in_id: int) -> None:
        if fill_in_id in self.__statements:
            del self.__statements[fill_in_id]
            print(f"FillInStatement with ID {fill_in_id} has been deleted.")
        else:
            raise KeyError(f"No FillInStatement exists with ID {fill_in_id} for deletion.")

    def find(self, filter_func: Callable[[FillInStatement], bool]) -> List[FillInStatement]:
        results: List[FillInStatement] = []
        for statement in self.__statements.values():
            if filter_func(statement):
                results.append(statement)
        return results