import sqlite3
from typing import Optional, List
import re

from backend.domain.entities.FillInStatement import FillInStatement


class FillInStatementRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
        self.TASK_TABLE = "quizz_tasks"

    def __parse_task_text(self, task_text: str) -> tuple[list[str], list[str]]:
        if not task_text:
            return [], []

        answers = re.findall(r'<([^>]+)>', task_text)

        segments_raw = re.split(r'<[^>]+>', task_text)
        text_segments = [s for s in segments_raw]

        return text_segments, answers

    def __build_task_text(self, segments: list[str], answers: list[str]) -> str:
        text = ""
        for i in range(max(len(segments), len(answers))):
            if i < len(segments):
                text += segments[i]
            if i < len(answers):
                text += f"<{answers[i]}>"
        return text

    def save(self, statement) -> None:
        task_text = self.__build_task_text(statement.get_text_segments(), statement._answer_list)

        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE id = ?", (statement._id,))
        exists = self.cursor.fetchone()

        quizz_id = statement.get_quizz_id()

        if exists:
            sql = f"UPDATE {self.TASK_TABLE} SET task_text = ?, type = ?, quizz = ? WHERE id = ?"
            self.cursor.execute(sql, (task_text, "fill-ins", quizz_id, statement._id))
        else:
            sql = f"INSERT INTO {self.TASK_TABLE} (id, task_text, type, quizz) VALUES (?, ?, ?, ?)"
            self.cursor.execute(sql, (statement._id, task_text, "fill-ins", quizz_id))

        self.conn.commit()

    def get_by_id(self, fill_in_id: int) -> Optional[object]:
        self.cursor.execute(f"SELECT id, task_text, quizz FROM {self.TASK_TABLE} WHERE id = ? AND type = 'fill-ins'",
                            (fill_in_id,))
        row = self.cursor.fetchone()

        if row:
            text_segments, answer_list = self.__parse_task_text(row[1])
            return FillInStatement(row[0], text_segments, answer_list, row[2])
        return None

    def delete_by_id(self, fill_in_id: int) -> None:
        self.cursor.execute(f"DELETE FROM {self.TASK_TABLE} WHERE id = ?", (fill_in_id,))
        self.conn.commit()

    def find(self, where_clause: str) -> List[object]:
        self.cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE type = 'fill-ins' AND {where_clause}")
        rows = self.cursor.fetchall()
        return [self.get_by_id(row[0]) for row in rows]