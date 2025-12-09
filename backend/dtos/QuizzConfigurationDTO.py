class QuizzConfigurationDTO:
    def __init__(self, difficulty: str, time_limit: int, tasks: list):
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.tasks = tasks  # list of DTOs
