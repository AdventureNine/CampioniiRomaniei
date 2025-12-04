import sqlite3
from typing import Optional, List, Callable, Any


class QuizzTaskRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TABLE = "quizz_tasks"

    def save(self, task) -> None:
        pass

    def get_by_id(self, task_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, type FROM {self.TABLE} WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()

        if row:
            return {"id": row[0], "type": row[1]}
        return None

    def get_all(self) -> List[object]:
        self.cursor.execute(f"SELECT id, type FROM {self.TABLE}")
        rows = self.cursor.fetchall()

        results = [{"id": row[0], "type": row[1]} for row in rows]
        return results

    def delete_by_id(self, task_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (task_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id, type FROM {self.TABLE} WHERE {where_clause}")
        rows = self.cursor.fetchall()

        results = [{"id": row[0], "type": row[1]} for row in rows]
        return results