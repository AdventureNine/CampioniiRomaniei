from typing import Optional, List
import sqlite3

from backend.domain.entities.Player import Player
from backend.domain.entities.Quizz import Quizz
from backend.domain.entities.Question import Question
from backend.domain.entities.FillInStatement import FillInStatement
from backend.domain.entities.Minigame import Minigame

from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository

from backend.service.PlayerService import PlayerService
from backend.service.QuizzService import QuizzService
from backend.service.QuestionService import QuestionService
from backend.service.FillInStatementService import FillInStatementService
from backend.service.MinigameService import MinigameService
from backend.service.QuizzTaskService import QuizzTaskService


class GameService:
    """
    Main game service that coordinates all game operations with a set player context.
    This service manages the overall game flow and interactions between different entities.
    """
    
    def __init__(self, conn: sqlite3.Connection):
        # Initialize repositories
        self.player_repository = PlayerRepository(conn)
        self.quizz_repository = QuizzRepository(conn)
        self.question_repository = QuestionRepository(conn)
        self.fill_in_repository = FillInStatementRepository(conn)
        self.minigame_repository = MinigameRepository(conn)
        self.quizz_task_repository = QuizzTaskRepository(conn)
        
        # Initialize services
        self.player_service = PlayerService(self.player_repository)
        self.quizz_service = QuizzService(self.quizz_repository)
        self.question_service = QuestionService(self.question_repository)
        self.fill_in_service = FillInStatementService(self.fill_in_repository)
        self.minigame_service = MinigameService(self.minigame_repository)
        self.quizz_task_service = QuizzTaskService(self.quizz_task_repository)
        
        # Current player context
        self.__current_player: Optional[Player] = None
    
    # Player Management
    def set_player(self, player: Player) -> None:
        """Set the current player context."""
        self.__current_player = player
    
    def get_current_player(self) -> Optional[Player]:
        """Get the current player."""
        return self.__current_player
    
    def load_player(self) -> bool:
        """Load the player from repository and set as current."""
        player = self.player_service.get_player()
        if player:
            self.__current_player = player
            return True
        return False
    
    def create_and_set_player(self, player_id: int, name: str) -> Player:
        """Create a new player and set as current."""
        player = self.player_service.create_player(player_id, name)
        self.__current_player = player
        return player
    
    def ensure_player(self) -> Player:
        """Ensure a player is set, raise error if not."""
        if self.__current_player is None:
            raise ValueError("No player is currently set. Please set a player first.")
        return self.__current_player
    
    # Player Operations
    def add_credits_to_player(self, amount: int) -> None:
        """Add credits to the current player."""
        player = self.ensure_player()
        self.player_service.add_credits(player, amount)
    
    def purchase_cosmetic(self, cosmetic: str, price: int) -> bool:
        """Purchase a cosmetic for the current player."""
        player = self.ensure_player()
        return self.player_service.purchase_cosmetic(player, cosmetic, price)
    
    def unlock_region(self, region: str) -> None:
        """Unlock a region for the current player."""
        player = self.ensure_player()
        self.player_service.unlock_region(player, region)
    
    def equip_cosmetic(self, cosmetic: str) -> bool:
        """Equip a cosmetic for the current player."""
        player = self.ensure_player()
        return self.player_service.equip_cosmetic(player, cosmetic)
    
    # Quizz Operations
    def start_quizz(self, quizz_id: int) -> Optional[Quizz]:
        """Start a quizz for the current player."""
        player = self.ensure_player()
        quizz = self.quizz_service.get_quizz_by_id(quizz_id)
        return quizz
    
    def complete_quizz(self, quizz: Quizz, is_solved: bool, play_time: float, credits_earned: int = 0) -> None:
        """
        Complete a quizz and update player statistics.
        
        Args:
            quizz: The completed quizz
            is_solved: Whether the quizz was successfully solved
            play_time: Time spent on the quizz in seconds
            credits_earned: Credits earned from completing the quizz
        """
        player = self.ensure_player()
        
        # Update quizz completion
        if is_solved:
            quizz.set_completion_percentage(100.0)
            self.quizz_service.update_quizz(quizz)
        
        # Update player statistics
        self.player_service.update_quizz_statistics(player, is_solved, play_time)
        
        # Award credits if earned
        if credits_earned > 0:
            self.player_service.add_credits(player, credits_earned)
    
    def update_quizz_progress(self, quizz: Quizz, completed_tasks: int) -> None:
        """Update the progress of a quizz based on completed tasks."""
        percentage = self.quizz_service.calculate_completion_percentage(quizz, completed_tasks)
        self.quizz_service.update_completion_percentage(quizz, percentage)
    
    def get_quizzes_by_difficulty(self, difficulty: str) -> List[Quizz]:
        """Get all quizzes with a specific difficulty."""
        return self.quizz_service.get_quizzes_by_difficulty(difficulty)
    
    # Question Operations
    def answer_question(self, question: Question, user_answers: List[str]) -> dict:
        """
        Answer a question and return the result.
        
        Returns:
            dict with 'correct' (bool), 'correct_answers' (list), and 'is_multiple_choice' (bool)
        """
        is_correct = self.question_service.check_answer(question, user_answers)
        
        return {
            "correct": is_correct,
            "correct_answers": self.question_service.get_correct_answers(question),
            "is_multiple_choice": self.question_service.is_multiple_choice(question)
        }
    
    def get_questions_for_quizz(self, quizz: Quizz) -> List[Question]:
        """Get all questions for a quizz."""
        return quizz.get_questions()
    
    # Fill-in Statement Operations
    def answer_fill_in(self, statement: FillInStatement, user_answers: List[str]) -> dict:
        """
        Answer a fill-in statement and return detailed results.
        
        Returns:
            dict with 'correct' (bool), 'total', 'correct_count', and 'details'
        """
        results = self.fill_in_service.check_partial_answers(statement, user_answers)
        
        return {
            "correct": results["correct"] == results["total"],
            "total": results["total"],
            "correct_count": results["correct"],
            "details": results["details"]
        }
    
    def get_fill_in_preview(self, statement: FillInStatement) -> str:
        """Get a preview of a fill-in statement with blanks."""
        return self.fill_in_service.get_statement_preview(statement)
    
    def get_fill_ins_for_quizz(self, quizz: Quizz) -> List[FillInStatement]:
        """Get all fill-in statements for a quizz."""
        return quizz.get_fill_in_statements()
    
    # Minigame Operations
    def play_minigame(self, minigame: Minigame) -> dict:
        """
        Get minigame info for playing.
        
        Returns:
            dict with 'type', 'win_configuration', and type-specific data
        """
        minigame_type = self.minigame_service.get_minigame_type(minigame)
        
        result = {
            "type": minigame_type,
            "win_configuration": minigame.get_win_configuration()
        }
        
        # Add type-specific data
        if minigame_type == "puzzle":
            result["image_path"] = self.minigame_service.get_puzzle_image_path(minigame)
        elif minigame_type == "rebus":
            result["questions"] = self.minigame_service.get_rebus_questions(minigame)
        elif minigame_type == "pairs":
            result["items"] = self.minigame_service.get_pairs_items(minigame)
        
        return result
    
    def check_minigame_completion(self, minigame: Minigame) -> bool:
        """Check if a minigame is completed correctly."""
        return self.minigame_service.check_win_condition(minigame)
    
    def get_minigames_for_quizz(self, quizz: Quizz) -> List[Minigame]:
        """Get all minigames for a quizz."""
        return quizz.get_minigames()
    
    # Overall Game Statistics
    def get_player_statistics(self) -> dict:
        """Get comprehensive statistics for the current player."""
        player = self.ensure_player()
        
        return {
            "player_name": player.get_name(),
            "credits": player.get_credits(),
            "avg_play_time": player.get_avg_play_time(),
            "quizzes_solved": player.get_quizzes_solved(),
            "quizzes_played": player.get_quizzes_played(),
            "regions_unlocked": player.get_regions_unlocked(),
            "completion_percentage": player.get_completion_percentage(),
            "cosmetics_unlocked": len(player.get_cosmetics_unlocked()),
            "cosmetics_purchased": len(player.get_cosmetics_purchased())
        }
    
    def get_game_progress(self) -> dict:
        """Get overall game progress for the current player."""
        player = self.ensure_player()
        task_stats = self.quizz_task_service.get_task_statistics()
        
        return {
            "player": {
                "name": player.get_name(),
                "credits": player.get_credits(),
                "completion_percentage": player.get_completion_percentage()
            },
            "tasks": task_stats,
            "regions_unlocked": len(player.get_regions_unlocked()),
            "quizzes_stats": {
                "solved": player.get_quizzes_solved(),
                "played": player.get_quizzes_played(),
                "success_rate": (player.get_quizzes_solved() / player.get_quizzes_played() * 100) 
                               if player.get_quizzes_played() > 0 else 0.0
            }
        }
    
    def calculate_and_update_overall_completion(self) -> float:
        """Calculate and update the player's overall game completion percentage."""
        player = self.ensure_player()
        
        # This is a simplified calculation - adjust based on your game logic
        # You might want to factor in: regions unlocked, quizzes completed, etc.
        total_regions = 10  # Adjust based on your game
        regions_unlocked = len(player.get_regions_unlocked())
        
        completion = (regions_unlocked / total_regions) * 100
        self.player_service.update_completion_percentage(player, completion)
        
        return completion
