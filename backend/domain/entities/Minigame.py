class Minigame:
    def __init__(self, minigame_id: int, win_configuration=None, current_configuration=None):
        self.__id = minigame_id
        self.__win_configuration = win_configuration
        self.__current_configuration = current_configuration

    def get_id(self): return self.__id
    def get_win_configuration(self): return self.__win_configuration
    def set_win_configuration(self, configuration): self.__win_configuration = configuration
    def get_current_configuration(self): return self.__current_configuration
    def set_current_configuration(self, configuration): self.__current_configuration = configuration

### Minigames:

class Puzzle(Minigame):
    ## Win Configuration created on the Frontend
    def __init__(self, puzzle_id: int, image_path: str): super().__init__(puzzle_id); self.__image_path = image_path
    def get_image_path(self): return self.__image_path
    def __str__(self): return f"Puzzle {self.get_id()}, Image path: {self.__image_path}"

class Rebus(Minigame):
    ## Win Configuration DB save format: "<question><answer>;<question><answer>;..."
    ## Win Configuration proposed format: {"question1": "answer1", "question2": "answer2", ...}
    def __init__(self, rebus_id: int, win_configuration): super().__init__(rebus_id, win_configuration)
    def __str__(self): return f"Rebus {self.get_id()}, Win configuration: {self.get_win_configuration()}"

class Bingo(Minigame):
    ## Win Configuration DB save format: "<bingo_cell1_text><true>;<bingo_cell2_text><false>;..."
    ## Current and Win Configurations proposed format: {"bingo_cell1_text": true, "bingo_cell2_text": false, ...}
    ## If win_configuration["bingo_cellX_text"] == true, then this cell is considered part of the bingo
    ## If current_configuration["bingo_cellX_text"] == true, then this cell is clicked by the player
    def __init__(self, bingo_id: int, win_configuration): super().__init__(bingo_id, win_configuration, [])
    def __str__(self): return f"Bingo {self.get_id()}, Win configuration: {self.get_win_configuration()}"

class Pairs(Minigame):
    ## Win Configuration DB save format: "<question><answer>;<question><answer>;..."
    ## Win Configuration proposed format: {"question1": "answer1", "question2": "answer2", ...}
    def __init__(self, pairs_id: int, win_configuration): super().__init__(pairs_id, win_configuration, [])
    def __str__(self): return f"Pairs {self.get_id()}, Win configuration: {self.get_win_configuration()}"

class MapGuesser(Minigame):
    ## Win Configuration DB save format: "<x><y>;<y><x>;..."
    ## Current and Win Configuration proposed format: [(x,y), (y,x), ...]
    def __init__(self, map_guesser_id: int, win_configuration): super().__init__(map_guesser_id, win_configuration, [])
    def __str__(self): return f"Map Guesser {self.get_id()}, Win configuration: {self.get_win_configuration()}"