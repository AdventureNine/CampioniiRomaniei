# backend/dto/DifficultyTimerDTO.py
class DifficultyTimerDTO:
    """
    Provides timer length in seconds for a difficulty string ('usor', 'mediu', 'greu').
    """
    DIFF_TO_SECONDS = {
        "usor": 5 * 60,   # 300
        "mediu": 7 * 60,  # 420
        "greu": 12 * 60   # 720
    }

    def __init__(self, difficulty: str):
        if not difficulty:
            raise ValueError("difficulty must be provided")
        self.difficulty = difficulty.lower()
        self.time_limit_seconds = self._map_time(self.difficulty)

    @classmethod
    def _map_time(cls, difficulty: str) -> int:
        if difficulty not in cls.DIFF_TO_SECONDS:
            raise ValueError(f"Invalid difficulty '{difficulty}'. Expected one of {list(cls.DIFF_TO_SECONDS.keys())}")
        return cls.DIFF_TO_SECONDS[difficulty]
