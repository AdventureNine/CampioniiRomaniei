from backend.repository.PlayerRepository import PlayerRepository
from backend.service.PlayerService import PlayerService
from backend.service.GameService import GameService
from backend.service.QuizzService import QuizzService
from backend.service.QuestionService import QuestionService
from backend.service.FillInStatementService import FillInStatementService
from backend.service.MinigameService import MinigameService
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository


def main():
    # Initialize repositories
    player_repo = PlayerRepository("backend/domain/data.db")
    quizz_repo = QuizzRepository("backend/domain/data.db")
    question_repo = QuestionRepository("backend/domain/data.db")
    fill_in_statement_repo = FillInStatementRepository("backend/domain/data.db")
    minigame_repo = MinigameRepository("backend/domain/data.db")

    # Initialize services
    player_service = PlayerService(player_repo)
    quizz_service = QuizzService(quizz_repo)
    question_service = QuestionService(question_repo)
    fill_in_statement_service = FillInStatementService(fill_in_statement_repo)
    minigame_service = MinigameService(minigame_repo)

    game_service = GameService(
        player_service,
        quizz_service,
        question_service,
        fill_in_statement_service,
        minigame_service
    )

    # Example usage
    game_service.set_player(1)  # Assuming player with id 1 exists
    regions = game_service.get_regions()
    print("Regions:", regions)

    tasks_region_1 = game_service.get_tasks(1)
    print("Tasks for Region 1:", tasks_region_1)


    # Complete a task
    game_service.complete_task(1, 1)
    tasks_region_1 = game_service.get_tasks(1)
    print("Tasks for Region 1 after completing task 1.1:", tasks_region_1)


if __name__ == "__main__":
    main()
