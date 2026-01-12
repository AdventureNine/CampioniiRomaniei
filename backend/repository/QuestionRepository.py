import sqlite3
from typing import Optional
from backend.domain.entities.Question import Question

class QuestionRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.TASK_TABLE = "quizz_tasks"
        self.ANSWER_TABLE = "answers"

    def save(self, question: Question, quizz_id: int) -> None:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE id = ?", (question.get_id(),))

        if cursor.fetchone():
            cursor.execute(f"UPDATE {self.TASK_TABLE} SET task_text = ?, type = ?, quizz = ? WHERE id = ?",(question.get_text(), "question", quizz_id, question.get_id()))
            cursor.execute(f"DELETE FROM {self.ANSWER_TABLE} WHERE quizz_task = ?", (question.get_id(),))
        else:
            cursor.execute(f"INSERT INTO {self.TASK_TABLE} (task_text, type, quizz) VALUES (?, ?, ?)",(question.get_text(), "question", quizz_id))

        answer_list = question.get_answer_list()
        ID = cursor.execute(f"SELECT seq FROM sqlite_sequence WHERE name = ?", ("quizz_tasks",)).fetchone()[0]
        for i in range(len(answer_list)):
            cursor.execute(f"INSERT INTO {self.ANSWER_TABLE} (answer_text, is_correct, quizz_task) VALUES (?, ?, ?)",
                           (answer_list[i], 1 if i==0 else 0, ID))
        self.conn.commit()

    def get_by_id(self, question_id: int) -> Optional[Question]:
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT id, task_text FROM {self.TASK_TABLE} WHERE id = ? AND type = 'question'",(question_id,))
        task_row = cursor.fetchone()
        if task_row:
            cursor.execute(f"SELECT answer_text, is_correct FROM {self.ANSWER_TABLE} WHERE quizz_task = ?",(question_id,))
            raw = [(row[0], row[1] == 1) for row in cursor.fetchall()]
            answer_data = []
            for t in raw:
                if t[1]: answer_data.insert(0, t[0])
                else: answer_data.append(t[0])
            return Question(task_row[0], task_row[1], answer_data)
        return None

    def find(self, where_clause: str) -> list[Question]:
        return [self.get_by_id(row[0]) for row in self.conn.cursor().execute(f"SELECT id FROM {self.TASK_TABLE} WHERE type = 'question' AND {where_clause}").fetchall()]