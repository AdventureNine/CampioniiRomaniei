import sqlite3
from typing import Optional
from backend.domain.entities.Quizz import Quizz

class QuizzRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.TABLE = "quizzes"
        self.TASK_TABLE = "quizz_tasks"

    def save(self, quizz, player_id) -> None:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (quizz.get_id(),))
        if cursor.fetchone():
            sql = f"UPDATE {self.TABLE} SET difficulty = ?, player = ? WHERE id = ?"
            cursor.execute(sql,(quizz.get_difficulty(), player_id, quizz.get_id()))
        else:
            sql = f"INSERT INTO {self.TABLE} (difficulty, player) VALUES (?, ?)"
            cursor.execute(sql, (quizz.get_difficulty(),player_id))

        self.conn.commit()

    def get_by_id(self, quizz_id: int) -> Optional[Quizz]:
        row = self.conn.cursor().execute(f"SELECT difficulty FROM {self.TABLE} WHERE id = ?", (quizz_id,)).fetchone()

        if row:
            quizz = Quizz(
                quizz_id=quizz_id,
                questions=[],
                fill_in_statements=[],
                minigames=None,
                difficulty=row[0]
            )
            return quizz
        return None

    def delete_by_id(self, quizz_id: int) -> None:
        self.conn.cursor().execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (quizz_id,))
        self.conn.commit()

    def find_all(self) -> list[Quizz]:
        return [self.get_by_id(row[0]) for row in self.conn.cursor().execute(f"SELECT id FROM {self.TABLE} ORDER BY id").fetchall()]