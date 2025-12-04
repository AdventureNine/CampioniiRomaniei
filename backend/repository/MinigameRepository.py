import sqlite3
from typing import Optional, List, Callable, Any
import json

from backend.domain.entities.Minigame import Minigame


class MinigameRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TASK_TABLE = "quizz_tasks"

    def save(self, minigame) -> None:
        win_config_json = json.dumps(minigame.get_win_configuration())

        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE id = ?", (minigame.get_id(),))
        exists = self.cursor.fetchone()

        quizz_id = minigame.get_quizz_id()

        if exists:
            sql = f"UPDATE {self.TASK_TABLE} SET task_text = ?, type = ?, quizz = ? WHERE id = ?"
            self.cursor.execute(sql, (win_config_json, "minigame", quizz_id, minigame.get_id()))
        else:
            sql = f"INSERT INTO {self.TASK_TABLE} (id, task_text, type, quizz) VALUES (?, ?, ?, ?)"
            self.cursor.execute(sql, (minigame.get_id(), win_config_json, "minigame", quizz_id))

        self.conn.commit()

    def get_by_id(self, minigame_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, task_text, quizz FROM {self.TASK_TABLE} WHERE id = ? AND type = 'minigame'",
                            (minigame_id,))
        row = self.cursor.fetchone()

        if row:
            win_config = json.loads(row[1])
            return Minigame(row[0], win_config, None, row[2])
        return None

    def delete_by_id(self, minigame_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TASK_TABLE} WHERE id = ?", (minigame_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE type = 'minigame' AND {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]