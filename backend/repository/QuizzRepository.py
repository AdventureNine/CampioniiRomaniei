import sqlite3
from typing import Optional, List

from backend.domain.entities.Quizz import Quizz
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.QuestionRepository import QuestionRepository


from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.QuestionRepository import QuestionRepository


class QuizzRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TABLE = "quizzes"
        self.TASK_TABLE = "quizz_tasks"
        self._question_repository = QuestionRepository(conn)
        self._fill_in_statement_repository = FillInStatementRepository(conn)
        self._minigame_repository = MinigameRepository(conn)

    def save(self, quizz) -> None:
        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (quizz.get_id(),))
        exists = self.cursor.fetchone()

        player_id = quizz.get_player().get_id()

        if exists:
            sql = f"""
                UPDATE {self.TABLE} 
                SET difficulty = ?, completion_percentage = ?, player = ?
                WHERE id = ?
            """
            self.cursor.execute(sql, (
                quizz.get_difficulty(), quizz.get_completion_percentage(),
                player_id, quizz.get_id()
            ))
        else:
            sql = f"""
                INSERT INTO {self.TABLE} (id, difficulty, completion_percentage, player) 
                VALUES (?, ?, ?, ?)
            """
            self.cursor.execute(sql, (
                quizz.get_id(), quizz.get_difficulty(), quizz.get_completion_percentage(),
                player_id
            ))

        self.conn.commit()

    def get_by_id(self, quizz_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, difficulty, completion_percentage FROM {self.TABLE} WHERE id = ?", (quizz_id,))
        row = self.cursor.fetchone()

        if row:
            questions = self._question_repository.get_all_by_quizz_id(quizz_id)
            fill_in_statements = self._fill_in_statement_repository.get_all_by_quizz_id(quizz_id)
            minigames = self._minigame_repository.get_all_by_quizz_id(quizz_id)

            quizz = Quizz(
                quizz_id=row[0],
                questions=questions,
                fill_in_statements=fill_in_statements,
                minigames=minigames,
                difficulty=row[1],
                completion_percentage=row[2]
            )
            return quizz
        return None

    def delete_by_id(self, quizz_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (quizz_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]