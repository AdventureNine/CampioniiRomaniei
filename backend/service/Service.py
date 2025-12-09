from random import random
import string

from backend.domain.entities.Minigame import Minigame
from backend.domain.entities.Player import Player
from backend.domain.entities.Question import Question
from backend.domain.entities.Quizz import Quizz
from backend.repository.FillInStatementRepository import FillInStatementRepository
from backend.repository.MinigameRepository import MinigameRepository
from backend.repository.PlayerRepository import PlayerRepository
from backend.repository.QuestionRepository import QuestionRepository
from backend.repository.QuizzRepository import QuizzRepository
from backend.repository.QuizzTaskRepository import QuizzTaskRepository

'''
  ar fi o chestie smechera ca noi sa verificam si daca playerul e mai vechi de 365 de zile, sa l stergem, 
  sau sa stergem la fiecare save de player, primul player care exista, atunci tot timpul exista 1 si acelasi in baza de date
  si nu riscam sa avem prea multi playeri in baza de date
'''


class Service:
    def __init__(self,
                 player_repository: PlayerRepository,
                 question_repository: QuestionRepository,
                 fill_in_statement_repository: FillInStatementRepository,
                 minigame_repository: MinigameRepository,
                 quizz_repository: QuizzRepository,
                 quizz_task_repository: QuizzTaskRepository):
        self.__player_repository = player_repository
        self.__question_repository = question_repository
        self.__fill_in_statement_repository = fill_in_statement_repository
        self.__minigame_repository = minigame_repository
        self.__quizz_repository = quizz_repository
        self.__quizz_task_repository = quizz_task_repository
        self.__player = None  # this player reprezents or the full player, or only the name of the player

    def set_player(self, name: str) -> Player:
        # e nevoie de un mic artificiu aici pt ca player are id si noi in repo nu folosim un player dto la adaugare care sa nu contina un id asa ca o sa pun asa random
        new_player = Player(999999, name)
        self.__player_repository.save(new_player)
        # aici pe baza numelui returnez id ul
        new_player.set_id(self.__player_repository.get_player_id_by_name(name))

        self.__player = new_player
        return new_player

    def get_player(self) -> Player:
        return self.__player

    def __get_random_question(self, number_of_questions: int) -> list[Question]:
        all_questions = self.__question_repository.get_all()
        selected_questions = []
        used_indices = set()

        while len(selected_questions) < number_of_questions:
            random_index = random.randint(0, len(all_questions) - 1)
            if random_index not in used_indices:
                used_indices.add(random_index)
                selected_questions.append(all_questions[random_index])

        return selected_questions
    
    
        
    def ___get_random_minigame(self, number_of_minigames: int) ->list[Minigame]:
        all_minigames = self.__minigame_repository.get_all()
        selected_minigames = []
        used_indices = set()
        # in caz ca am dori mai multe minigame uri in viitor, putem schimba conditia din while
        while len(selected_minigames) < number_of_minigames:
            random_index = random.randint(0, len(all_minigames) - 1)
            if random_index not in used_indices:
                used_indices.add(random_index)
                selected_minigames.append(all_minigames[random_index])

        return selected_minigames
    
    def get_random_quizz(self) -> Quizz:
        quizzes = self.__quizz_repository.get_all()
        random_index = random.randint(0, len(quizzes) - 1)
        return quizzes[random_index]
    

    # def get_generated_quizz(self) -> Quizz:
    #     quiz = self.__quizz_repository.get_all()
    #     questions = self.__get_random_question(6)
    #     minigames = self.___get_random_minigame(1)
    #     fill_in_statements = []  # momentan nu avem fill in statements
    #     quizz = Quizz(questions)
    #     return quizz
    
    
    def save_player(self, player: Player) -> None:
        self.__player_repository.save(player)
        
    def get_player_by_id(self, player_id: int) -> Player:
        return self.__player_repository.get_by_id(player_id)
    
    def save_quizz(self, quizz: Quizz) -> None:
        self.__quizz_repository.save(quizz)
    
        

