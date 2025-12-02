from typing import Optional, List, Callable, Any
from backend.domain.entities.Player import Player


class PlayerRepository:
    def __init__(self):
        self.__players: dict[int, Player] = {}

    def save(self, player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError("Object must be of type Player.")

        player_id = player.get_id()
        self.__players[player_id] = player

    def get_by_id(self, player_id: int) -> Optional[Player]:
        return self.__players.get(player_id)

    def get_all(self) -> List[Player]:
        return list(self.__players.values())

    def delete_by_id(self, player_id: int) -> None:
        if player_id in self.__players:
            del self.__players[player_id]
        else:
            raise KeyError(f"No Player exists with ID {player_id} for deletion.")

    def find(self, filter_func: Callable[[Player], bool]) -> List[Player]:
        results: List[Player] = []
        for player in self.__players.values():
            if filter_func(player):
                results.append(player)
        return results