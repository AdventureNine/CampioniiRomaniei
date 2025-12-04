import sqlite3
from typing import Optional, List, Callable, Any
from backend.domain.entities.QuizzTask import QuizzTask

class QuizzTaskRepository:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()
        self.TABLE = "QuizzTask"

    def __serialize_list(self, data_list: list[str]) -> str:
        return ",".join(data_list)

    def __deserialize_string(self, data_string: str) -> list[str]:
        return data_string.split(',') if data_string else []

    def save(self, task: QuizzTask) -> None:
        answer_list_str = self.__serialize_list(task._answer_list)

        self.cursor.execute(f"SELECT id FROM {self.TABLE} WHERE id = ?", (task._id,))

        if self.cursor.fetchone():
            sql = f"UPDATE {self.TABLE} SET answer_list = ? WHERE id = ?"
            self.cursor.execute(sql, (answer_list_str, task._id))
        else:
            sql = f"INSERT INTO {self.TABLE} (id, answer_list) VALUES (?, ?)"
            self.cursor.execute(sql, (task._id, answer_list_str))

        self.conn.commit()

    def get_by_id(self, task_id: int) -> Optional[QuizzTask]:
        self.cursor.execute(f"SELECT id, answer_list FROM {self.TABLE} WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()

        if row:
            answer_list = self.__deserialize_string(row[1])
            return QuizzTask(row[0], answer_list)
        return None

    def get_all(self) -> List[QuizzTask]:
        self.cursor.execute(f"SELECT id, answer_list FROM {self.TABLE}")
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            answer_list = self.__deserialize_string(row[1])
            results.append(QuizzTask(row[0], answer_list))

        return results

    def delete_by_id(self, task_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TABLE} WHERE id = ?", (task_id,))

        if self.cursor.rowcount == 0:
            raise KeyError(f"No QuizzTask exists with ID {task_id} for deletion.")

        self.conn.commit()

    def find(self, where_clause: str) -> List[QuizzTask]:
        sql = f"SELECT id, answer_list FROM {self.TABLE} WHERE {where_clause}"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        results = []
        for row in rows:
            answer_list = self.__deserialize_string(row[1])
            results.append(QuizzTask(row[0], answer_list))

        return results