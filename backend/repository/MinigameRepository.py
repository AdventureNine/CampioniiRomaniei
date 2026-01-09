import sqlite3
from typing import Optional, List, Callable, Any
import json
import re

from backend.domain.entities.Minigame import Minigame, Puzzle, Rebus, Bingo, Pairs, MapGuesser


class MinigameRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TABLE = "minigames"

    def __get_type_string(self, minigame) -> str:
        if isinstance(minigame, Puzzle): return "puzzle"
        if isinstance(minigame, Rebus): return "rebus"
        if isinstance(minigame, Bingo): return "bingo"
        if isinstance(minigame, Pairs): return "pairs"
        if isinstance(minigame, MapGuesser): return "map_guesser"
        return "minigame"

    def __format_win_config(self, minigame) -> str:
        config = minigame.get_win_configuration()

        if isinstance(minigame, Puzzle):
            return str(minigame.get_image_path())

        if isinstance(minigame, (Rebus, Pairs)):
            return "".join([f"<{k}><{v}>;" for k, v in config.items()])

        if isinstance(minigame, Bingo):
            return "".join([f"<{k}><{str(v).lower()}>;" for k, v in config.items()])

        if isinstance(minigame, MapGuesser):
            return "".join([f"<{x}><{y}>;" for x, y in config])

        return str(config)

    def __parse_win_config(self, raw_str: str, m_type: str):
        if not raw_str: return None
        if m_type == "puzzle": return raw_str

        pairs = re.findall(r'<(.*?)><(.*?)>', raw_str)

        if m_type in ["rebus", "pairs"]:
            return {k: v for k, v in pairs}

        if m_type == "bingo":
            return {k: (v.lower() == 'true') for k, v in pairs}

        if m_type == "map_guesser":
            return [(int(x), int(y)) for x, y in pairs]

        return raw_str

    def save(self, minigame) -> None:
        win_config_str = self.__format_win_config(minigame)
        task_type = self.__get_type_string(minigame)
        quizz_id = minigame.get_quizz_id()

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (minigame.get_id(),))
        exists = self.cursor.fetchone()

        if exists:
            sql = f"UPDATE {self.TABLE} SET win_configuration = ?, type = ?, quizz = ? WHERE id = ?"
            self.cursor.execute(sql, (win_config_str, task_type, quizz_id, minigame.get_id()))
        else:
            sql = f"INSERT INTO {self.TABLE} (id, win_configuration, type, quizz) VALUES (?, ?, ?, ?)"
            self.cursor.execute(sql, (minigame.get_id(), win_config_str, task_type, quizz_id))

        self.conn.commit()

    def get_by_id(self, minigame_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, win_configuration, quizz, type FROM {self.TABLE} WHERE id = ?",
                            (minigame_id,))
        row = self.cursor.fetchone()

        if row:
            m_id, raw_config, q_id, m_type = row
            win_config = self.__parse_win_config(raw_config, m_type)

            if m_type == "puzzle":
                return Puzzle(m_id, win_config)
            elif m_type == "rebus":
                return Rebus(m_id, win_config)
            elif m_type == "bingo":
                return Bingo(m_id, win_config)
            elif m_type == "pairs":
                return Pairs(m_id, win_config)
            elif m_type == "map_guesser":
                return MapGuesser(m_id, win_config)

            return Minigame(m_id, win_config, None, q_id)
        return None

    def delete_by_id(self, minigame_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (minigame_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]