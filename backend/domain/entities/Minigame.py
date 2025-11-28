class Minigame:
    def __init__(self, minigame_id: int, win_configuration=None, current_configuration=None):
        self.__id = minigame_id
        self.__win_configuration = win_configuration
        self.__current_configuration = current_configuration

    def get_id(self): return self.__id
    def get_win_configuration(self): return self.__win_configuration
    def get_current_configuration(self): return self.__current_configuration
    def set_current_configuration(self, configuration): self.__current_configuration = configuration

# TODO: minigames

class Puzzle(Minigame):
    def __init__(self, puzzle_id: int, win_configuration):
        super().__init__(puzzle_id, win_configuration,[])
        # just a small example