

class MinigameDTO:
    def __init__(self, minigame_id: int, win_configuration: dict, region: str):
        self.id = minigame_id
        self.win_configuration = win_configuration
        self.region = region
