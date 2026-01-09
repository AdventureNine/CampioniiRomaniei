import sqlite3
from typing import Optional, List, Callable, Any
import json

from backend.domain.entities.Minigame import Minigame, Puzzle, Rebus, Bingo, Pairs, MapGuesser


class MinigameRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TASK_TABLE = "quizz_tasks"

    def __get_type_string(self, minigame) -> str:
        if isinstance(minigame, Puzzle): return "puzzle"
        if isinstance(minigame, Rebus): return "rebus"
        if isinstance(minigame, Bingo): return "bingo"
        if isinstance(minigame, Pairs): return "pairs"
        if isinstance(minigame, MapGuesser): return "map_guesser"
        return "minigame"

    def save(self, minigame) -> None:
        win_config = minigame.get_win_configuration()

        if isinstance(minigame, Puzzle):
            if win_config is None: win_config = {}
            win_config["image_path"] = minigame.get_image_path()

        win_config_json = json.dumps(win_config)
        task_type = self.__get_type_string(minigame)

        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE id = ?", (minigame.get_id(),))
        exists = self.cursor.fetchone()

        quizz_id = minigame.get_quizz_id()

        if exists:
            sql = f"UPDATE {self.TASK_TABLE} SET task_text = ?, type = ?, quizz = ? WHERE id = ?"
            self.cursor.execute(sql, (win_config_json, task_type, quizz_id, minigame.get_id()))
        else:
            sql = f"INSERT INTO {self.TASK_TABLE} (id, task_text, type, quizz) VALUES (?, ?, ?, ?)"
            self.cursor.execute(sql, (minigame.get_id(), win_config_json, task_type, quizz_id))

        self.conn.commit()

    def get_by_id(self, minigame_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, task_text, quizz, type FROM {self.TASK_TABLE} WHERE id = ?",
                            (minigame_id,))
        row = self.cursor.fetchone()

        if row:
            m_id, task_text, quizz_id, m_type = row
            win_config = json.loads(task_text) if task_text else {}

            if m_type == "puzzle":
                return Puzzle(m_id, win_config.get("image_path", ""))
            elif m_type == "rebus":
                return Rebus(m_id, win_config)
            elif m_type == "bingo":
                return Bingo(m_id, win_config)
            elif m_type == "pairs":
                return Pairs(m_id, win_config)
            elif m_type == "map_guesser":
                return MapGuesser(m_id, win_config)

            return Minigame(m_id, win_config, None, quizz_id)
        return None

    def delete_by_id(self, minigame_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TASK_TABLE} WHERE id = ?", (minigame_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]