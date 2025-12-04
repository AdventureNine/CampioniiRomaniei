import sqlite3
from typing import Optional, List, Callable, Any
from backend.domain.entities.Question import Question

class QuestionRepository:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.TABLE = "Question"

    def __serialize_list(self, data_list: list[str]) -> str:
        return ",".join(data_list)

    def __deserialize_string(self, data_string: str) -> list[str]:
        return data_string.split(',') if data_string else []

    def save(self, question: Question) -> None:
        answer_list_str = self.__serialize_list(question._answer_list)

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (question._id,))

        if self.cursor.fetchone():
            sql = f"UPDATE {self.TABLE} SET text = ?, answer_list = ? WHERE id = ?"
            self.cursor.execute(sql, (question.get_text(), answer_list_str, question._id))
        else:
            sql = f"INSERT INTO {self.TABLE} (id, text, answer_list) VALUES (?, ?, ?)"
            self.cursor.execute(sql, (question._id, question.get_text(), answer_list_str))

        self.conn.commit()

    def get_by_id(self, question_id: int) -> Optional[Question]:
        self.cursor.execute(f"SELECT id, text, answer_list FROM {self.TABLE} WHERE id = ?", (question_id,))
        row = self.cursor.fetchone()

        if row:
            answer_list = self.__deserialize_string(row[2])
            return Question(row[0], row[1], answer_list)
        return None

    def get_all(self) -> List[Question]:
        self.cursor.execute(f"SELECT id, text, answer_list FROM {self.TABLE}")
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            answer_list = self.__deserialize_string(row[2])
            results.append(Question(row[0], row[1], answer_list))

        return results

    def delete_by_id(self, question_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (question_id,))

        if self.cursor.rowcount == 0:
            raise KeyError(f"No Question exists with ID {question_id} for deletion.")

        self.conn.commit()

    def find(self, where_clause: str) -> List[Question]:
        sql = f"SELECT id, text, answer_list FROM {self.TABLE} WHERE {where_clause}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            answer_list = self.__deserialize_string(row[2])
            results.append(Question(row[0], row[1], answer_list))

        return results