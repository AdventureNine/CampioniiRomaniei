from backend.domain.entities.Question import Question
from backend.domain.entities.FillInStatement import FillInStatement
from backend.domain.entities.Minigame import Minigame

class Quizz:
    def __init__(self, quizz_id: int, questions: list[Question], fill_in_statements: list[FillInStatement], minigames: list[Minigame], difficulty: str):
        self.__id = quizz_id
        self.__difficulty = difficulty
        self.__questions = questions
        self.__fill_in_statements = fill_in_statements
        self.__minigames = minigames

    def get_id(self): return self.__id
    def get_questions(self): return self.__questions
    def get_fill_in_statements(self): return self.__fill_in_statements
    def get_minigames(self): return self.__minigames
    def get_difficulty(self): return self.__difficulty

    def __str__(self): return f"Quizz {self.__id} ({self.__difficulty}) with {len(self.__questions)} questions, {len(self.__fill_in_statements)} fill-in statements, {len(self.__minigames)} minigames and difficulty \"{self.__difficulty}\"."