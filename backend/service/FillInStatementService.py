from backend.domain.entities.FillInStatement import FillInStatement
from backend.repository.FillInStatementRepository import FillInStatementRepository


class FillInStatementService:
    def __init__(self, repository: FillInStatementRepository):
        self._repository = repository

    def create_fill_in_statement(self, fill_in_id: int, quizz_id: int, text_segments: list[str], answer_list: list[str]) -> FillInStatement:
        statement = FillInStatement(fill_in_id, text_segments, answer_list)
        self._repository.save(statement, quizz_id)
        return statement

    def get_fill_in_statement(self, fill_in_id: int) -> FillInStatement:
        return self._repository.get_by_id(fill_in_id)

    def get_fill_in_statements_by_quizz(self, quizz_id: int) -> list[FillInStatement]:
        return self._repository.get_all(quizz_id)

    def update_fill_in_statement(self, fill_in_id: int, new_text_segments: list[str], new_answer_list: list[str]) -> FillInStatement:
        statement = self._repository.get_by_id(fill_in_id)
        if statement:
            updated_statement = FillInStatement(fill_in_id, new_text_segments, new_answer_list)
            self._repository.update(updated_statement)
            return updated_statement
        return None

    def delete_fill_in_statement(self, fill_in_id: int):
        self._repository.delete(fill_in_id)
