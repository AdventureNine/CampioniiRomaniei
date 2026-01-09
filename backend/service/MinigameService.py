from typing import Optional, List
from backend.repository.MinigameRepository import MinigameRepository
from backend.domain.entities.Minigame import Minigame, Puzzle, Rebus, Bingo, Pairs, MapGuesser


class MinigameService:
    def __init__(self, minigame_repository: MinigameRepository):
        self.minigame_repository = minigame_repository

    def create_minigame(self, minigame: Minigame) -> None:
        """Create and save a new minigame."""
        self.minigame_repository.save(minigame)

    def get_minigame_by_id(self, minigame_id: int) -> Optional[Minigame]:
        """Get a minigame by its ID."""
        return self.minigame_repository.get_by_id(minigame_id)

    def update_minigame(self, minigame: Minigame) -> None:
        """Update an existing minigame."""
        self.minigame_repository.save(minigame)

    def delete_minigame(self, minigame_id: int) -> None:
        """Delete a minigame by ID."""
        self.minigame_repository.delete_by_id(minigame_id)

    def check_win_condition(self, minigame: Minigame) -> bool:
        """Check if the current configuration matches the win configuration."""
        win_config = minigame.get_win_configuration()
        current_config = minigame.get_current_configuration()
        
        if win_config is None or current_config is None:
            return False
        
        return win_config == current_config

    def reset_minigame(self, minigame: Minigame) -> None:
        """Reset the minigame to initial state."""
        minigame.set_current_configuration(None)
        self.minigame_repository.save(minigame)

    # Puzzle-specific methods
    def get_puzzle_image_path(self, puzzle: Puzzle) -> str:
        """Get the image path for a puzzle minigame."""
        if isinstance(puzzle, Puzzle):
            return puzzle.get_image_path()
        return ""

    # Rebus-specific methods
    def check_rebus_answer(self, rebus: Rebus, question: str, user_answer: str) -> bool:
        """Check if a rebus answer is correct."""
        if isinstance(rebus, Rebus):
            win_config = rebus.get_win_configuration()
            if isinstance(win_config, dict) and question in win_config:
                return win_config[question].strip().lower() == user_answer.strip().lower()
        return False

    def get_rebus_questions(self, rebus: Rebus) -> List[str]:
        """Get all questions from a rebus minigame."""
        if isinstance(rebus, Rebus):
            win_config = rebus.get_win_configuration()
            if isinstance(win_config, dict):
                return list(win_config.keys())
        return []

    # Bingo-specific methods
    def toggle_bingo_cell(self, bingo: Bingo, cell_text: str) -> None:
        """Toggle a bingo cell on/off."""
        if isinstance(bingo, Bingo):
            current_config = bingo.get_current_configuration()
            if current_config is None:
                current_config = {}
            
            if cell_text in current_config:
                current_config[cell_text] = not current_config[cell_text]
            else:
                current_config[cell_text] = True
            
            bingo.set_current_configuration(current_config)
            self.minigame_repository.save(bingo)

    def check_bingo_win(self, bingo: Bingo) -> bool:
        """Check if the bingo configuration is complete."""
        if isinstance(bingo, Bingo):
            win_config = bingo.get_win_configuration()
            current_config = bingo.get_current_configuration()
            
            if not isinstance(win_config, dict) or not isinstance(current_config, dict):
                return False
            
            for cell, required_state in win_config.items():
                if required_state and current_config.get(cell, False) != True:
                    return False
            
            return True
        return False

    # Pairs-specific methods
    def check_pair_match(self, pairs: Pairs, question: str, answer: str) -> bool:
        """Check if a pair match is correct."""
        if isinstance(pairs, Pairs):
            win_config = pairs.get_win_configuration()
            if isinstance(win_config, dict):
                return win_config.get(question, "").strip().lower() == answer.strip().lower()
        return False

    def get_pairs_items(self, pairs: Pairs) -> dict:
        """Get all pairs items."""
        if isinstance(pairs, Pairs):
            return pairs.get_win_configuration() or {}
        return {}

    # MapGuesser-specific methods
    def check_map_location(self, map_guesser: MapGuesser, x: float, y: float, tolerance: float = 0.1) -> bool:
        """Check if a map location is correct within tolerance."""
        if isinstance(map_guesser, MapGuesser):
            win_config = map_guesser.get_win_configuration()
            if isinstance(win_config, list):
                for wx, wy in win_config:
                    if abs(wx - x) <= tolerance and abs(wy - y) <= tolerance:
                        return True
        return False

    def add_map_guess(self, map_guesser: MapGuesser, x: float, y: float) -> None:
        """Add a location guess to the map guesser."""
        if isinstance(map_guesser, MapGuesser):
            current_config = map_guesser.get_current_configuration()
            if current_config is None:
                current_config = []
            
            current_config.append((x, y))
            map_guesser.set_current_configuration(current_config)
            self.minigame_repository.save(map_guesser)

    def get_minigame_type(self, minigame: Minigame) -> str:
        """Get the type of minigame as a string."""
        if isinstance(minigame, Puzzle):
            return "puzzle"
        elif isinstance(minigame, Rebus):
            return "rebus"
        elif isinstance(minigame, Bingo):
            return "bingo"
        elif isinstance(minigame, Pairs):
            return "pairs"
        elif isinstance(minigame, MapGuesser):
            return "map_guesser"
        return "unknown"
