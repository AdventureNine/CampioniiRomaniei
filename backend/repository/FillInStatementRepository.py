import sqlite3, re
from typing import Optional
from backend.domain.entities.FillInStatement import FillInStatement

def _parse_task_text(task_text: str) -> tuple[list[str], list[str]]:
    if not task_text: return [], []
    answers = re.findall(r'<([^>]+)>', task_text)
    segments_raw = re.split(r'(<[^>]+>)', task_text)
    text_segments = [s.strip() for s in segments_raw if s and not s.startswith('<')]
    return text_segments, answers

def _build_task_text(segments: list[str], answers: list[str]) -> str:
    text = ""
    for i in range(max(len(segments), len(answers))):
        if i < len(segments): text += segments[i]
        if i < len(answers): text += f"<{answers[i]}>"
    return text


class FillInStatementRepository:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.TASK_TABLE = "quizz_tasks"

    def save(self, statement: FillInStatement, quizz_id: int) -> None:
        cursor = self.conn.cursor()
        task_text = _build_task_text(statement.get_text_segments(), statement.get_answer_list())
        cursor.execute(f"SELECT id FROM {self.TASK_TABLE} WHERE id = ?", (statement.get_id(),))

        if cursor.fetchone():
            sql = f"UPDATE {self.TASK_TABLE} SET task_text = ?, type = ?, quizz = ? WHERE id = ?"
            cursor.execute(sql, (task_text, "fill-ins", quizz_id, statement.get_id()))
        else:
            sql = f"INSERT INTO {self.TASK_TABLE} (task_text, type, quizz) VALUES (?, ?, ?)"
            cursor.execute(sql, (task_text, "fill-ins", quizz_id))

        self.conn.commit()

    def get_by_id(self, fill_in_id: int) -> Optional[FillInStatement]:
        row = self.conn.cursor().execute(f"SELECT id, task_text FROM {self.TASK_TABLE} WHERE id = ? AND type = 'fill-ins'",(fill_in_id,)).fetchone()
        if row:
            text_segments, answer_list = _parse_task_text(row[1])
            return FillInStatement(row[0], text_segments, answer_list)
        return None

    def find(self, where_clause: str) -> list[FillInStatement]:
        return [self.get_by_id(row[0]) for row in self.conn.cursor().execute(f"SELECT id FROM {self.TASK_TABLE} WHERE type = 'fill-ins' AND {where_clause}").fetchall()]
