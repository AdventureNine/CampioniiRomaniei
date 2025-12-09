from backend.domain.entities.Minigame import Minigame, Puzzle
from backend.repository.MinigameRepository import MinigameRepository


class MinigameService:
    def __init__(self, repository: MinigameRepository):
        self._repository = repository

    def create_minigame(self, minigame_id: int, quizz_id: int, win_configuration, current_configuration=None) -> Minigame:
        minigame = Minigame(minigame_id, win_configuration, current_configuration)
        self._repository.add(minigame, quizz_id)
        return minigame

    def create_puzzle(self, puzzle_id: int, quizz_id: int, win_configuration) -> Puzzle:
        puzzle = Puzzle(puzzle_id, win_configuration)
        self._repository.add(puzzle, quizz_id)
        return puzzle

    def get_minigame(self, minigame_id: int) -> Minigame:
        return self._repository.get_by_id(minigame_id)

    def get_minigames_by_quizz(self, quizz_id: int) -> list[Minigame]:
        return self._repository.get_all(quizz_id)

    def update_minigame_configuration(self, minigame_id: int, new_current_configuration) -> Minigame:
        minigame = self._repository.get_by_id(minigame_id)
        if minigame:
            minigame.set_current_configuration(new_current_configuration)
            self._repository.update(minigame)
            return minigame
        return None

    def delete_minigame(self, minigame_id: int):
        self._repository.delete(minigame_id)
