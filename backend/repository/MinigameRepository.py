import sqlite3, re
from typing import Optional
from backend.domain.entities.Minigame import Minigame, Puzzle, Rebus, Bingo, Pairs, MapGuesser

def _parse_win_config(raw_str: str, m_type: str):
    if not raw_str: return None
    if m_type == "puzzle": return raw_str
    pairs = re.findall(r'<(.*?)><(.*?)>', raw_str)
    if m_type in ["rebus", "pairs"]: return {k: v for k, v in pairs}
    if m_type == "bingo": return {k: (v.lower() == 'true') for k, v in pairs}
    if m_type == "map_guesser": return [(float(x), float(y)) for x, y in pairs]
    return raw_str

def _format_win_config(minigame) -> str:
    config = minigame.get_win_configuration()
    if isinstance(minigame, Puzzle): return str(minigame.get_image_path())
    if isinstance(minigame, (Rebus, Pairs)): return "".join([f"<{k}><{v}>;" for k, v in config.items()])
    if isinstance(minigame, Bingo): return "".join([f"<{k}><{str(v).lower()}>;" for k, v in config.items()])
    if isinstance(minigame, MapGuesser): return "".join([f"<{x}><{y}>;" for x, y in config])
    return str(config)

def _get_type_string(minigame) -> str:
    if isinstance(minigame, Puzzle): return "puzzle"
    if isinstance(minigame, Rebus): return "rebus"
    if isinstance(minigame, Bingo): return "bingo"
    if isinstance(minigame, Pairs): return "pairs"
    if isinstance(minigame, MapGuesser): return "map_guesser"
    return "minigame"


class MinigameRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.TABLE = "minigames"

    def save(self, minigame: Minigame, quizz_id: int) -> None:
        win_config_str = _format_win_config(minigame)
        task_type = _get_type_string(minigame)
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (minigame.get_id(),))

        if cursor.fetchone():
            sql = f"UPDATE {self.TABLE} SET win_configuration = ?, type = ?, quizz = ? WHERE id = ?"
            cursor.execute(sql, (win_config_str, task_type, quizz_id, minigame.get_id()))
        else:
            sql = f"INSERT INTO {self.TABLE} (win_configuration, type, quizz) VALUES (?, ?, ?)"
            cursor.execute(sql, (win_config_str, task_type, quizz_id))

        self.conn.commit()

    def get_by_id(self, minigame_id: int) -> Optional[Minigame]:
        row = self.conn.cursor().execute(f"SELECT id, win_configuration, type FROM {self.TABLE} WHERE id = ?",(minigame_id,)).fetchone()

        if row:
            m_id, raw_config, m_type = row
            win_config = _parse_win_config(raw_config, m_type)
            if m_type == "puzzle": return Puzzle(m_id, win_config)
            elif m_type == "rebus": return Rebus(m_id, win_config)
            elif m_type == "bingo": return Bingo(m_id, win_config)
            elif m_type == "pairs": return Pairs(m_id, win_config)
            elif m_type == "map_guesser": return MapGuesser(m_id, win_config)
            return Minigame(m_id, win_config, None)

        return None

    def delete_by_id(self, minigame_id: int) -> None:
        self.conn.cursor().execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (minigame_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> list[Minigame]:
        return [self.get_by_id(row[0]) for row in self.conn.cursor().execute(f"SELECT id FROM {self.TABLE} WHERE {where_clause}").fetchall()]