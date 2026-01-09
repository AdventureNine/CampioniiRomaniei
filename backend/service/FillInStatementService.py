from typing import Optional, List
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.domain.entities.FillInStatement import FillInStatement


class FillInStatementService:
    def __init__(self, fill_in_repository: FillInStatementRepository):
        self.fill_in_repository = fill_in_repository

    def create_fill_in_statement(self, statement: FillInStatement) -> None:
        """Create and save a new fill-in statement."""
        self.fill_in_repository.save(statement)

    def get_fill_in_by_id(self, fill_in_id: int) -> Optional[FillInStatement]:
        """Get a fill-in statement by its ID."""
        return self.fill_in_repository.get_by_id(fill_in_id)

    def update_fill_in_statement(self, statement: FillInStatement) -> None:
        """Update an existing fill-in statement."""
        self.fill_in_repository.save(statement)

    def delete_fill_in_statement(self, fill_in_id: int) -> None:
        """Delete a fill-in statement by ID."""
        self.fill_in_repository.delete_by_id(fill_in_id)

    def find_fill_in_statements(self, where_clause: str) -> List[FillInStatement]:
        """Find fill-in statements matching a where clause."""
        return self.fill_in_repository.find(where_clause)

    def check_answers(self, statement: FillInStatement, user_answers: List[str]) -> bool:
        """Check if the user's answers are correct."""
        return statement.check_answers(user_answers)

    def get_blank_count(self, statement: FillInStatement) -> int:
        """Get the number of blanks in the fill-in statement."""
        return len(statement.get_answer_list())

    def get_statement_preview(self, statement: FillInStatement) -> str:
        """Get a preview of the statement with blanks represented as underscores."""
        preview = ""
        segments = statement.get_text_segments()
        answers = statement.get_answer_list()
        
        for i in range(max(len(segments), len(answers))):
            if i < len(segments):
                preview += segments[i]
            if i < len(answers):
                preview += "____"
        
        return preview

    def validate_statement_structure(self, statement: FillInStatement) -> bool:
        """Validate that the statement has proper structure (at least one blank)."""
        return len(statement.get_answer_list()) > 0

    def get_fill_ins_by_quizz(self, quizz_id: int) -> List[FillInStatement]:
        """Get all fill-in statements for a specific quizz."""
        return self.fill_in_repository.find(f"quizz = {quizz_id}")

    def check_partial_answers(self, statement: FillInStatement, user_answers: List[str]) -> dict:
        """Check answers and return detailed results for each blank."""
        correct_answers = statement.get_answer_list()
        results = {
            "total": len(correct_answers),
            "correct": 0,
            "details": []
        }
        
        for i, user_answer in enumerate(user_answers):
            if i < len(correct_answers):
                is_correct = user_answer.strip().lower() == correct_answers[i].strip().lower()
                if is_correct:
                    results["correct"] += 1
                results["details"].append({
                    "index": i,
                    "user_answer": user_answer,
                    "correct_answer": correct_answers[i],
                    "is_correct": is_correct
                })
        
        return results
