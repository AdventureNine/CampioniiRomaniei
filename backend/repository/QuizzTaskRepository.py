import sqlite3
from typing import Optional

class QuizzTaskRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.TABLE = "quizz_tasks"

    def get_by_id(self, task_id: int) -> Optional[dict[str, int | str]]:
        row = self.conn.cursor().execute(f"SELECT id, type FROM {self.TABLE} WHERE id = ?", (task_id,)).fetchone()
        if row: return {"id": row[0], "type": row[1]}
        return None

    def get_all(self) -> list[dict[str, int | str]]:
        return [{"id": row[0], "type": row[1]} for row in self.conn.cursor().execute(f"SELECT id, type FROM {self.TABLE}").fetchall()]

    def delete_by_id(self, task_id: int) -> None:
        self.conn.cursor().execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (task_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> list[dict[str, int | str]]:
        return [{"id": row[0], "type": row[1]} for row in self.conn.cursor().execute(f"SELECT id, type FROM {self.TABLE} WHERE {where_clause}").fetchall()]
