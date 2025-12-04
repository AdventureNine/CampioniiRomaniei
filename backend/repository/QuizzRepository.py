import sqlite3
from typing import Optional, List, Callable, Any
from backend.domain.entities.Quizz import Quizz

class QuizzRepository:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.TABLE = "Quizz"

    def __serialize_id_list(self, entity_list: list) -> str:
        return ",".join(map(lambda x: str(x.get_id() if hasattr(x, 'get_id') else x._id), entity_list))

    def __deserialize_string(self, data_string: str) -> list:
        return [int(i) for i in data_string.split(',')] if data_string else []

    def save(self, quizz: Quizz) -> None:
        questions_ids = self.__serialize_id_list(quizz.get_questions())
        fill_in_ids = self.__serialize_id_list(quizz.get_fill_in_statements())
        minigame_ids = self.__serialize_id_list(quizz.get_minigames())

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (quizz.get_id(),))

        if self.cursor.fetchone():
            sql = f"""
                UPDATE {self.TABLE} 
                SET difficulty = ?, completion_percentage = ?, 
                questions_ids = ?, fill_in_ids = ?, minigame_ids = ? 
                WHERE id = ?
            """
            self.cursor.execute(sql, (quizz.get_difficulty(), quizz.get_completion_percentage(),
                                      questions_ids, fill_in_ids, minigame_ids, quizz.get_id()))
        else:
            sql = f"""
                INSERT INTO {self.TABLE} (id, difficulty, completion_percentage, questions_ids, fill_in_ids, minigame_ids) 
                VALUES (?, ?, ?, ?, ?, ?)
            """
            self.cursor.execute(sql, (quizz.get_id(), quizz.get_difficulty(), quizz.get_completion_percentage(),
                                      questions_ids, fill_in_ids, minigame_ids))

        self.conn.commit()

    def get_by_id(self, quizz_id: int) -> Optional[Quizz]:
        self.cursor.execute(f"SELECT * FROM {self.TABLE} WHERE id = ?", (quizz_id,))
        row = self.cursor.fetchone()

        if row:
            q_ids = self.__deserialize_string(row[3])
            f_ids = self.__deserialize_string(row[4])
            m_ids = self.__deserialize_string(row[5])

            return Quizz(row[0], q_ids, f_ids, m_ids, row[1], row[2])
        return None

    def get_all(self) -> List[Quizz]:
        self.cursor.execute(f"SELECT * FROM {self.TABLE}")
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            q_ids = self.__deserialize_string(row[3])
            f_ids = self.__deserialize_string(row[4])
            m_ids = self.__deserialize_string(row[5])
            results.append(Quizz(row[0], q_ids, f_ids, m_ids, row[1], row[2]))

        return results

    def delete_by_id(self, quizz_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (quizz_id,))

        if self.cursor.rowcount == 0:
            raise KeyError(f"No Quizz exists with ID {quizz_id} for deletion.")

        self.conn.commit()

    def find(self, where_clause: str) -> List[Quizz]:
        sql = f"SELECT * FROM {self.TABLE} WHERE {where_clause}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            q_ids = self.__deserialize_string(row[3])
            f_ids = self.__deserialize_string(row[4])
            m_ids = self.__deserialize_string(row[5])
            results.append(Quizz(row[0], q_ids, f_ids, m_ids, row[1], row[2]))

        return results