from typing import Optional
from backend.domain.entities.Player import Player
from backend.domain.entities.Quizz import Quizz
from backend.domain.entities.Question import Question
from backend.domain.entities.Minigame import MapGuesser, Minigame, Rebus, Bingo, Puzzle, Pairs
from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository

def convert_MapGuesser_to_frontend_format(map_guesser: MapGuesser) -> dict:
    """Convert a MapGuesser minigame to frontend-compatible format."""
    config = map_guesser.get_win_configuration() or {}
    targets = [{'question': k, 'x': v[0], 'y': v[1]} for k, v in config.items()]
    return {
        'type': 'map_guess',
        'targets': targets
    }

def convert_question_to_frontend_format(question: Question) -> dict:
    """Convert a Question to frontend-compatible format."""
    answers = question.get_answer_list()
    return {
        'type': 'quizz',
        'id': question.get_id(),
        'question': question.get_text(),
        'options': answers,
        'correct': answers[0] if answers else ''
    }


def convert_fill_to_frontend_format(fill) -> dict:
    return {
        "type": "fill",
        "question": "".join(fill.get_text_segments()),
        "correct": fill.get_answer_list()
    }


def _get_region_name_by_id(region_id: int) -> str | None:
    match region_id:
        case 1: return "Transilvania"
        case 2: return "Moldova"
        case 3: return "Țara Românească"
        case 4: return "Dobrogea"
        case 5: return "Banat"
    return None


class Service:
    def __init__(self, player_repository: PlayerRepository,
                    question_repository: QuestionRepository,
                    fill_in_repository: FillInStatementRepository,
                    minigame_repository: MinigameRepository,
                    quizz_repository: QuizzRepository,
                    quizz_task_repository: QuizzTaskRepository
                ):
        self.__player_repository = player_repository
        self.__question_repository = question_repository
        self.__fill_in_repository = fill_in_repository
        self.__minigame_repository = minigame_repository
        self.__quizz_repository = quizz_repository
        self.__quizz_task_repository = quizz_task_repository

    def get_player(self) -> Optional[Player]: return self.__player_repository.get()

    def save_player(self, player: Player) -> None:
        if player: self.__player_repository.save(player)

    def add_credits(self, amount: int) -> int:
        """Add credits to current player. Returns new total."""
        player = self.get_player()
        if player:
            new_credits = player.get_credits() + amount
            player.set_credits(new_credits)
            self.save_player(player)
            return new_credits
        return 0

    def spend_credits(self, amount: int) -> bool:
        """Spend credits. Returns True if successful."""
        player = self.get_player()
        if player and player.get_credits() >= amount:
            player.set_credits(player.get_credits() - amount)
            self.save_player(player)
            return True
        return False

    def purchase_cosmetic(self, cosmetic_path: str, cost: int) -> bool:
        """Purchase a cosmetic if player has enough credits."""
        player = self.get_player()
        if player and player.get_credits() >= cost:
            purchased = player.get_cosmetics_purchased()
            if cosmetic_path not in purchased:
                purchased.append(cosmetic_path)
                player.set_cosmetics_purchased(purchased)
                player.set_credits(player.get_credits() - cost)
                self.save_player(player)
                return True
        return False

    def equip_cosmetic(self, cosmetic_path: str) -> bool:
        """Equip a cosmetic if owned."""
        player = self.get_player()
        if player and cosmetic_path in player.get_cosmetics_purchased():
            player.set_cosmetic(cosmetic_path)
            self.save_player(player)
            return True
        return False

    def get_player_stats(self) -> Optional[dict]:
        """Get player statistics as dict."""
        player = self.get_player()
        if player:
            return {
                "name": player.get_name(),
                "credits": player.get_credits(),
                "avg_play_time": player.get_avg_play_time(),
                "quizzes_solved": player.get_quizzes_solved(),
                "quizzes_played": player.get_quizzes_played(),
                "completion_percentage": player.get_completion_percentage(),
                "regions_state": player.get_regions_state(),
                "equipped_cosmetic": player.get_cosmetic(),
                "cosmetics_owned": player.get_cosmetics_purchased()
            }
        return None

    def increment_quizzes_played(self) -> None:
        """Increment quizzes played count."""
        player = self.get_player()
        if player:
            player.set_quizzes_played(player.get_quizzes_played() + 1)
            self.save_player(player)

    def increment_quizzes_solved(self) -> None:
        """Increment quizzes solved count."""
        player = self.get_player()
        if player:
            player.set_quizzes_solved(player.get_quizzes_solved() + 1)
            self.save_player(player)

    def update_play_time(self, session_time: float) -> None:
        """Update average playtime with new session time."""
        player = self.get_player()
        if player:
            played = player.get_quizzes_played()
            current_avg = player.get_avg_play_time()
            new_avg = ((current_avg * played) + session_time) / (played + 1) if played > 0 else session_time
            player.set_avg_play_time(new_avg)
            self.save_player(player)

    def is_level_unlocked(self, region_id: int, level_index: int) -> bool:
        region_status = self.__player_repository.get().get_regions_state()
        region_name = _get_region_name_by_id(region_id)
        if region_status[region_name] >= level_index: return True
        return False

    def get_quizz_by_id(self, quizz_id: int) -> Optional[Quizz]:

        quizz: Quizz = self.__quizz_repository.get_by_id(quizz_id)
        questions = self.__question_repository.find(f"quizz = {quizz_id}")
        fill_ins = self.__fill_in_repository.find(f"quizz = {quizz_id}")
        minigames = self.__minigame_repository.find(f"quizz = {quizz_id}")[0]

        quizz.set_questions(questions)
        quizz.set_fill_in_statements(fill_ins)
        quizz.set_minigame(minigames)

        return quizz

    def get_level_data(self, quizz_id: int) -> list[dict]:
        """
        Returnează pașii unui nivel în ordinea din DB
        """
        tasks = self.__quizz_task_repository.find(
            f"quizz = {quizz_id} ORDER BY id"
        )

        level_steps: list[dict] = []

        for task in tasks:
            task_id = task["id"]
            task_type = task["type"]

            if task_type == "question":
                q = self.__question_repository.get_by_id(task_id)
                if q:
                    level_steps.append(
                        convert_question_to_frontend_format(q)
                    )

            elif task_type == "fill-ins":
                f = self.__fill_in_repository.get_by_id(task_id)
                if f:
                    level_steps.append(
                        convert_fill_to_frontend_format(f)
                    )

        quizz = self.get_quizz_by_id(quizz_id)

        if quizz:
            minigame = quizz.get_minigames()

            if minigame and isinstance(minigame, Rebus):
                level_steps.append({"type": "rebus"})
            if minigame and isinstance(minigame, Bingo):
                level_steps.append({"type": "bingo"})
            if minigame and isinstance(minigame, MapGuesser):
                level_steps.append({"type": "map_guesser"})
            if minigame and isinstance(minigame, Puzzle):
                level_steps.append({"type": "puzzle"})
            if minigame and isinstance(minigame, Pairs):
                level_steps.append({"type": "pairs"})
        return level_steps

    def get_minigame_by_id(self, minigame_id: int):
        return self.__minigame_repository.get_by_id(minigame_id)