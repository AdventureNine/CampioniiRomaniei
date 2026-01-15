from backend.domain.entities.Question import Question
from backend.domain.entities.FillInStatement import FillInStatement
from backend.domain.entities.Minigame import Minigame

class Quizz:
    def __init__(self, quizz_id: int, questions: list[Question], fill_in_statements: list[FillInStatement], minigame:Minigame|None, difficulty: str):
        self.__id = quizz_id
        self.__difficulty = difficulty
        self.__questions = questions
        self.__fill_in_statements = fill_in_statements
        self.__minigame = minigame

    def get_id(self): return self.__id
    def get_questions(self): return self.__questions
    def get_fill_in_statements(self): return self.__fill_in_statements
    def get_minigames(self): return self.__minigame
    def get_difficulty(self): return self.__difficulty
    def set_questions(self, questions: list[Question]): self.__questions = questions
    def set_fill_in_statements(self, fill_ins: list[FillInStatement]): self.__fill_in_statements = fill_ins
    def set_minigame(self, minigame: Minigame): self.__minigame = minigame

    def __str__(self): return f"Quizz {self.__id} ({self.__difficulty}) with {len(self.__questions)} questions, {len(self.__fill_in_statements)} fill-in statements, {self.__minigame} minigames and difficulty \"{self.__difficulty}\"."