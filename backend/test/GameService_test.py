import sys
import os
import unittest
import sqlite3

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.service.FillInStatementService import FillInStatementService
from backend.service.GameService import GameService
from backend.service.MinigameService import MinigameService
from backend.service.PlayerService import PlayerService
from backend.service.QuestionService import QuestionService
from backend.service.QuizzService import QuizzService


class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect("backend/test/data-test.db")
        self.player_repo = PlayerRepository(self.conn)
        self.quizz_repo = QuizzRepository(self.conn)
        self.question_repo = QuestionRepository(self.conn)
        self.fill_in_statement_repo = FillInStatementRepository(self.conn)
        self.minigame_repo = MinigameRepository(self.conn)

        # Initialize services
        self.player_service = PlayerService(self.player_repo)
        self.quizz_service = QuizzService(self.quizz_repo)
        self.question_service = QuestionService(self.question_repo)
        self.fill_in_statement_service = FillInStatementService(self.fill_in_statement_repo)
        self.minigame_service = MinigameService(self.minigame_repo)

        self.game_service = GameService(
            self.player_service,
            self.quizz_service,
            self.question_service,
            self.fill_in_statement_service,
            self.minigame_service
        )

        # Add a test player to the database
        with open("backend/test/data-test.db", "w") as f:
            f.write("")
        self.conn.cursor().execute(
            "CREATE TABLE player (id INTEGER, name TEXT, credits INTEGER, avg_play_time REAL, quizzes_solved INTEGER, quizzes_played INTEGER, regions_unlocked TEXT, cosmetics_unlocked TEXT, cosmetics_purchased TEXT, completion_percentage REAL)")
        self.conn.cursor().execute(
            "INSERT INTO player (id, name, credits, avg_play_time, quizzes_solved, quizzes_played, regions_unlocked, cosmetics_unlocked, cosmetics_purchased, completion_percentage) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (1, 'test_player', 0, 0.0, 0, 0, '[]', '[]', '[]', 0.0))
        self.conn.commit()

    def test_game_service(self):
        # Set player
        self.game_service.set_player(1)
        self.assertIsNotNone(self.game_service._player)

        # Get regions
        regions = self.game_service.get_regions()
        self.assertEqual(len(regions), 5)
        self.assertTrue(regions[0]["unlocked"])
        self.assertFalse(regions[1]["unlocked"])

        # Get tasks
        tasks = self.game_service.get_tasks(1)
        self.assertEqual(len(tasks), 6)
        self.assertTrue(tasks[0]["unlocked"])
        self.assertFalse(tasks[1]["unlocked"])

        # Complete a task
        self.game_service.complete_task(1, 1)
        tasks = self.game_service.get_tasks(1)
        self.assertFalse(tasks[0]["unlocked"])
        self.assertTrue(tasks[1]["unlocked"])

        # Complete all tasks in a region
        for i in range(1, 6):
            self.game_service.complete_task(1, i + 1)

        tasks = self.game_service.get_tasks(1)
        self.assertTrue(all(not task["unlocked"] for task in tasks))

        # Check if next region is unlocked
        regions = self.game_service.get_regions()
        self.assertTrue(regions[1]["unlocked"])


if __name__ == '__main__':
    unittest.main()
