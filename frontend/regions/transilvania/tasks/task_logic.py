import random


class TaskLogic:
    def __init__(self, questions, task_number):
        self.questions = questions
        self.task_number = task_number
        self.current_difficulty = None
        self.current_question = None
        self.correct_answer = None

    def get_random_question(self):
        self.current_difficulty, qlist = random.choice(list(self.questions.items()))
        self.current_question, self.correct_answer = random.choice(qlist)
        return self.current_difficulty, self.current_question

    def check_answer(self, user_answer):
        if not user_answer or not self.correct_answer:
            return False
        return user_answer.strip().lower() == self.correct_answer.strip().lower()

    def is_final_task(self):
        return self.task_number == 4

