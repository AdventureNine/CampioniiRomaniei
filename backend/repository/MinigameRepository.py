from typing import Optional, List, Callable, Any
from backend.domain.entities.Minigame import Minigame, Puzzle


class MinigameRepository:

    def __init__(self):
        self.__minigames: dict[int, Minigame] = {}

    def save(self, minigame: Minigame) -> None:
        if not isinstance(minigame, Minigame):
            raise TypeError("Object must be of type Minigame or a subclass thereof.")

        game_id = minigame.get_id()
        self.__minigames[game_id] = minigame

    def get_by_id(self, minigame_id: int) -> Optional[Minigame]:
        return self.__minigames.get(minigame_id)

    def get_all(self) -> List[Minigame]:
        return list(self.__minigames.values())

    def delete_by_id(self, minigame_id: int) -> None:
        if minigame_id in self.__minigames:
            del self.__minigames[minigame_id]
        else:
            raise KeyError(f"No Minigame exists with ID {minigame_id} for deletion.")

    def find(self, filter_func: Callable[[Minigame], bool]) -> List[Minigame]:
        results: List[Minigame] = []
        for minigame in self.__minigames.values():
            if filter_func(minigame):
                results.append(minigame)
        return results