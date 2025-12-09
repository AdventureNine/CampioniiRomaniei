from backend.domain.entities.Player import Player
from backend.domain.utils.Difficulty import Difficulty
from backend.dtos.QuestionDTO import QuestionDTO
from backend.dtos.QuizDataDTO import QuizDataDTO
from backend.service.FillInStatementService import FillInStatementService
from backend.service.MinigameService import MinigameService
from backend.service.PlayerService import PlayerService
from backend.service.QuestionService import QuestionService
from backend.service.QuizzService import QuizzService


class MainService:
    def __init__(self,
                 player_service: PlayerService,
                 question_service: QuestionService,
                 fill_in_statement_service: FillInStatementService,
                 minigame_service: MinigameService,
                 quizz_service: QuizzService):
        self._player_service = player_service
        self._question_service = question_service
        self._fill_in_statement_service = fill_in_statement_service
        self.minigame_service = minigame_service
        self._quizz_service = quizz_service
        self._player = None

    def set_player(self, player_id: int):
        self._player = self._player_service.get_player(player_id)

    def get_quiz_data(self, difficulty: str) -> QuizDataDTO:
        if difficulty not in Difficulty:
            raise ValueError("Invalid difficulty level")

        quizzes = self._quizz_service.get_quizzes_by_difficulty(difficulty)
        questions = []
        for quizz in quizzes:
            questions.extend(self._question_service.get_questions_by_quizz(quizz.get_id()))

        # Assuming we need 6 questions as per the request
        questions = questions[:6]

        question_dtos = [QuestionDTO(q.get_text(), q.get_answer_list()) for q in questions]

        timer = 0
        if difficulty == "Usor":
            timer = 5 * 60
        elif difficulty == "Mediu":
            timer = 7 * 60
        elif difficulty == "Dificil":
            timer = 10 * 60

        return QuizDataDTO(question_dtos, timer)
