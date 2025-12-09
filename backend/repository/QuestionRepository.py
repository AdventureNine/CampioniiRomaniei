import sqlite3
from typing import Optional, List

from backend.domain.entities.Question import Question


class QuestionRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TASK_TABLE = "quizz_tasks"
        self.ANSWER_TABLE = "answers"

    def save(self, question) -> None:
        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE id = ?", (question._id,))
        exists = self.cursor.fetchone()

        quizz_id = question.get_quizz_id()

        if exists:
            self.cursor.execute(f"UPDATE {self.TASK_TABLE} SET task_text = ?, type = ?, quizz = ? WHERE id = ?",
                                (question.get_text(), "question", quizz_id, question._id))

            self.cursor.execute(f"DELETE FROM {self.ANSWER_TABLE} WHERE quizz_task = ?", (question._id,))
        else:
            self.cursor.execute(f"INSERT INTO {self.TASK_TABLE} (id, task_text, type, quizz) VALUES (?, ?, ?, ?)",
                                (question._id, question.get_text(), "question", quizz_id))

        for answer_data in question.get_answer_data():
            answer_text, is_correct = answer_data
            self.cursor.execute(
                f"INSERT INTO {self.ANSWER_TABLE} (answer_text, is_correct, quizz_task) VALUES (?, ?, ?)",
                (answer_text, 1 if is_correct else 0, question._id))

        self.conn.commit()

    def get_by_id(self, question_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, task_text, quizz FROM {self.TASK_TABLE} WHERE id = ? AND type = 'question'",
                            (question_id,))
        task_row = self.cursor.fetchone()

        if task_row:
            self.cursor.execute(f"SELECT answer_text, is_correct FROM {self.ANSWER_TABLE} WHERE quizz_task = ?",
                                (question_id,))
            answer_rows = self.cursor.fetchall()

            answer_data = [(row[0], row[1] == 1) for row in answer_rows]

            return Question(task_row[0], task_row[1], answer_data, task_row[2])
        return None

    def delete_by_id(self, question_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TASK_TABLE} WHERE id = ?", (question_id,))
        self.conn.commit()

    def get_all_by_quizz_id(self, quizz_id: int) -> List[Question]:
        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE quizz = ? AND type = 'question'", (quizz_id,))
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE type = 'question' AND {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]