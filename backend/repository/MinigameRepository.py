import sqlite3
from typing import Optional, List, Callable, Any
from backend.domain.entities.Minigame import Minigame

class MinigameRepository:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.TABLE = "Minigame"

    def __serialize_list(self, data_list: list) -> str:
        return ",".join(map(str, data_list))

    def __deserialize_string(self, data_string: str) -> list:
        return data_string.split(',') if data_string else []

    def save(self, minigame: Minigame) -> None:
        win_config_str = self.__serialize_list(minigame.get_win_configuration())
        current_config_str = self.__serialize_list(minigame.get_current_configuration())

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (minigame.get_id(),))

        if self.cursor.fetchone():
            sql = f"UPDATE {self.TABLE} SET win_configuration = ?, current_configuration = ? WHERE id = ?"
            self.cursor.execute(sql, (win_config_str, current_config_str, minigame.get_id()))
        else:
            sql = f"INSERT INTO {self.TABLE} (id, win_configuration, current_configuration) VALUES (?, ?, ?)"
            self.cursor.execute(sql, (minigame.get_id(), win_config_str, current_config_str))

        self.conn.commit()

    def get_by_id(self, minigame_id: int) -> Optional[Minigame]:
        self.cursor.execute(f"SELECT id, win_configuration, current_configuration FROM {self.TABLE} WHERE id = ?",
                            (minigame_id,))
        row = self.cursor.fetchone()

        if row:
            win_config = self.__deserialize_string(row[1])
            current_config = self.__deserialize_string(row[2])
            return Minigame(row[0], win_config, current_config)
        return None

    def get_all(self) -> List[Minigame]:
        self.cursor.execute(f"SELECT id, win_configuration, current_configuration FROM {self.TABLE}")
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            win_config = self.__deserialize_string(row[1])
            current_config = self.__deserialize_string(row[2])
            results.append(Minigame(row[0], win_config, current_config))

        return results

    def delete_by_id(self, minigame_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (minigame_id,))

        if self.cursor.rowcount == 0:
            raise KeyError(f"No Minigame exists with ID {minigame_id} for deletion.")

        self.conn.commit()

    def find(self, where_clause: str) -> List[Minigame]:
        sql = f"SELECT id, win_configuration, current_configuration FROM {self.TABLE} WHERE {where_clause}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            win_config = self.__deserialize_string(row[1])
            current_config = self.__deserialize_string(row[2])
            results.append(Minigame(row[0], win_config, current_config))

        return results