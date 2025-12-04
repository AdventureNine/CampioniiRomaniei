import sqlite3
from typing import Optional, List, Callable, Any
from backend.domain.entities.FillInStatement import FillInStatement

class FillInStatementRepository:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.TABLE = "FillInStatement"

    def __serialize_list(self, data_list: list[str]) -> str:
        return ",".join(data_list)

    def __deserialize_string(self, data_string: str) -> list[str]:
        return data_string.split(',') if data_string else []

    def save(self, statement: FillInStatement) -> None:
        text_segments_str = self.__serialize_list(statement.get_text_segments())
        answer_list_str = self.__serialize_list(statement._answer_list)

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (statement._id,))

        if self.cursor.fetchone():
            sql = f"""
                UPDATE {self.TABLE} 
                SET text_segments = ?, answer_list = ? 
                WHERE id = ?
            """
            self.cursor.execute(sql, (text_segments_str, answer_list_str, statement._id))
        else:
            sql = f"""
                INSERT INTO {self.TABLE} (id, text_segments, answer_list) 
                VALUES (?, ?, ?)
            """
            self.cursor.execute(sql, (statement._id, text_segments_str, answer_list_str))

        self.conn.commit()

    def get_by_id(self, fill_in_id: int) -> Optional[FillInStatement]:
        self.cursor.execute(f"SELECT id, text_segments, answer_list FROM {self.TABLE} WHERE id = ?", (fill_in_id,))
        row = self.cursor.fetchone()

        if row:
            text_segments = self.__deserialize_string(row[1])
            answer_list = self.__deserialize_string(row[2])
            return FillInStatement(row[0], text_segments, answer_list)
        return None

    def get_all(self) -> List[FillInStatement]:
        self.cursor.execute(f"SELECT id, text_segments, answer_list FROM {self.TABLE}")
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            text_segments = self.__deserialize_string(row[1])
            answer_list = self.__deserialize_string(row[2])
            results.append(FillInStatement(row[0], text_segments, answer_list))

        return results

    def delete_by_id(self, fill_in_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (fill_in_id,))

        if self.cursor.rowcount == 0:
            raise KeyError(f"No FillInStatement exists with ID {fill_in_id} for deletion.")

        self.conn.commit()

    def find(self, where_clause: str) -> List[FillInStatement]:
        sql = f"SELECT id, text_segments, answer_list FROM {self.TABLE} WHERE {where_clause}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            text_segments = self.__deserialize_string(row[1])
            answer_list = self.__deserialize_string(row[2])
            results.append(FillInStatement(row[0], text_segments, answer_list))

        return results