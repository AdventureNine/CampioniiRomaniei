class Player:
    def __init__(self, pid: int, name: str):
        self.__id = pid
        self.__name = name
        self.__credits = 0
        self.__cosmetic = "/backend/domain/cosmetics/default.png"
        self.__statistics = {
            "avg_play_time": 0.0,
            "quizzes_solved": 0,
            "quizzes_played": 0,
            "regions_state": {},
            "cosmetics_purchased": [self.__cosmetic],
            "completion_percentage": 0.0
        }

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def set_name(self, name: str): self.__name = name
    def get_credits(self): return self.__credits
    def set_credits(self, new_credits: int): self.__credits = new_credits
    def get_cosmetic(self): return self.__cosmetic
    def set_cosmetic(self, new_cosmetic: str): self.__cosmetic = new_cosmetic
    def get_statistics(self): return self.__statistics

    def get_avg_play_time(self): return self.__statistics["avg_play_time"]
    def get_quizzes_solved(self): return self.__statistics["quizzes_solved"]
    def get_quizzes_played(self): return self.__statistics["quizzes_played"]
    def get_regions_unlocked(self): return self.__statistics["regions_unlocked"]
    def get_completion_percentage(self): return self.__statistics["completion_percentage"]
    def get_cosmetics_purchased(self): return self.__statistics["cosmetics_purchased"]

    def set_avg_play_time(self, avg_play_time: float): self.__statistics["avg_play_time"] = avg_play_time
    def set_quizzes_solved(self, quizzes_solved: int): self.__statistics["quizzes_solved"] = quizzes_solved
    def set_quizzes_played(self, quizzes_played: int): self.__statistics["quizzes_played"] = quizzes_played
    def set_regions_state(self, regions_state: dict[str,int]): self.__statistics["regions_state"] = regions_state
    def set_completion_percentage(self, completion_percentage: float): self.__statistics["completion_percentage"] = completion_percentage
    def set_cosmetics_purchased(self, cosmetics_purchased: list[str]): self.__statistics["cosmetics_purchased"] = cosmetics_purchased

    def __str__(self): return f"Player {self.__name} (id: {self.__id})\nCredits: {self.__credits} \nEquipped cosmetic {self.__cosmetic} \nStatistics: {self.__statistics}"