import sqlite3
from typing import Optional, List

from backend.domain.entities.Quizz import Quizz


class QuizzRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TABLE = "quizzes"
        self.TASK_TABLE = "quizz_tasks"

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
        self.cursor.execute(f"SELECT * FROM {self.TABLE} WHERE id = ?", (quizz_id,))
        row = self.cursor.fetchone()

        if row:
            self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE quizz = ?", (quizz_id,))
            task_rows = self.cursor.fetchall()
            task_ids = [row[0] for row in task_rows]

            quizz = Quizz(row[0], row[1], None)
            quizz.set_completion_percentage(row[2])
            quizz._Quizz__task_ids = task_ids
            return quizz
        return None

    def delete_by_id(self, quizz_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (quizz_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]