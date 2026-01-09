from typing import Optional
from backend.repository.PlayerRepository import PlayerRepository
from backend.domain.entities.Player import Player


class PlayerService:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def create_player(self, player_id: int, name: str) -> Player:
        """Create a new player and save it to the repository."""
        player = Player(player_id, name)
        self.player_repository.save(player)
        return player

    def get_player(self) -> Optional[Player]:
        """Get the current player."""
        return self.player_repository.get()

    def get_player_by_name(self, name: str) -> Optional[Player]:
        """Get a player by their username."""
        return self.player_repository.get_by_name(name)

    def update_player(self, player: Player) -> None:
        """Update an existing player."""
        self.player_repository.save(player)

    def delete_player(self, player_id: int) -> None:
        """Delete a player by ID."""
        self.player_repository.delete(player_id)

    def add_credits(self, player: Player, amount: int) -> None:
        """Add credits to a player."""
        current_credits = player.get_credits()
        player.set_credits(current_credits + amount)
        self.player_repository.save(player)

    def deduct_credits(self, player: Player, amount: int) -> bool:
        """Deduct credits from a player. Returns True if successful, False if insufficient credits."""
        current_credits = player.get_credits()
        if current_credits >= amount:
            player.set_credits(current_credits - amount)
            self.player_repository.save(player)
            return True
        return False

    def unlock_region(self, player: Player, region: str) -> None:
        """Unlock a new region for the player."""
        regions = player.get_regions_unlocked()
        if region not in regions:
            regions.append(region)
            player.set_regions_unlocked(regions)
            self.player_repository.save(player)

    def unlock_cosmetic(self, player: Player, cosmetic: str) -> None:
        """Unlock a new cosmetic for the player."""
        cosmetics = player.get_cosmetics_unlocked()
        if cosmetic not in cosmetics:
            cosmetics.append(cosmetic)
            player.set_cosmetics_unlocked(cosmetics)
            self.player_repository.save(player)

    def purchase_cosmetic(self, player: Player, cosmetic: str, price: int) -> bool:
        """Purchase a cosmetic. Returns True if successful, False if insufficient credits."""
        if self.deduct_credits(player, price):
            cosmetics_purchased = player.get_cosmetics_purchased()
            if cosmetic not in cosmetics_purchased:
                cosmetics_purchased.append(cosmetic)
                player.set_cosmetics_purchased(cosmetics_purchased)
                self.player_repository.save(player)
            return True
        return False

    def equip_cosmetic(self, player: Player, cosmetic: str) -> bool:
        """Equip a cosmetic. Returns True if successful, False if cosmetic not unlocked."""
        if cosmetic in player.get_cosmetics_unlocked():
            player.set_cosmetic(cosmetic)
            self.player_repository.save(player)
            return True
        return False

    def update_quizz_statistics(self, player: Player, is_solved: bool, play_time: float) -> None:
        """Update player statistics after completing a quizz."""
        # Update quizzes played
        quizzes_played = player.get_quizzes_played() + 1
        player.set_quizzes_played(quizzes_played)

        # Update quizzes solved if applicable
        if is_solved:
            quizzes_solved = player.get_quizzes_solved() + 1
            player.set_quizzes_solved(quizzes_solved)

        # Update average play time
        current_avg = player.get_avg_play_time()
        new_avg = ((current_avg * (quizzes_played - 1)) + play_time) / quizzes_played
        player.set_avg_play_time(new_avg)

        self.player_repository.save(player)

    def update_completion_percentage(self, player: Player, percentage: float) -> None:
        """Update the player's overall completion percentage."""
        player.set_completion_percentage(percentage)
        self.player_repository.save(player)
