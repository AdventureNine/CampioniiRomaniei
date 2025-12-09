from backend.domain.entities.Player import Player
from backend.repository.PlayerRepository import PlayerRepository


class PlayerService:
    def __init__(self, repository: PlayerRepository):
        self._repository = repository

    def create_player(self, pid: int, name: str) -> Player:
        player = Player(pid, name)
        self._repository.save(player)
        return player

    def get_player(self, player_id: int) -> Player:
        return self._repository.get_by_id(player_id)

    def get_all_players(self) -> list[Player]:
        return self._repository.get_all()

    def update_player_name(self, player_id: int, new_name: str) -> Player:
        player = self._repository.get_by_id(player_id)
        if player:
            player.set_name(new_name)
            self._repository.save(player)
            return player
        return None

    def add_credits(self, player_id: int, amount: int) -> Player:
        player = self._repository.get_by_id(player_id)
        if player:
            current_credits = player.get_credits()
            player.set_credits(current_credits + amount)
            self._repository.save(player)
            return player
        return None

    def purchase_cosmetic(self, player_id: int, cosmetic: str, cost: int) -> Player:
        player = self._repository.get_by_id(player_id)
        if player:
            if player.get_credits() >= cost:
                player.set_credits(player.get_credits() - cost)
                cosmetics = player.get_cosmetics_purchased()
                cosmetics.append(cosmetic)
                player.set_cosmetics_purchased(cosmetics)
                self._repository.save(player)
                return player
        return None
