import random


class TaskLogic:
    def __init__(self, questions, task_number):
        self.questions = questions
        self.task_number = task_number
        self.current_question_index = 0
        self.selected_questions = []
        self.correct_answers = 0
        self.setup_task()

    def setup_task(self):
        answer_questions = [q for q in self.questions if q['type'] == 'answer']
        fill_questions = [q for q in self.questions if q['type'] == 'fill_in']

        selected_answers = random.sample(answer_questions, min(3, len(answer_questions)))
        selected_fills = random.sample(fill_questions, min(2, len(fill_questions)))

        self.selected_questions = selected_answers + selected_fills
        random.shuffle(self.selected_questions)
        self.current_question_index = 0
        self.correct_answers = 0

    def get_current_question(self):
        if self.current_question_index < len(self.selected_questions):
            q = self.selected_questions[self.current_question_index]
            return {
                'difficulty': q['difficulty'],
                'question': q['question'],
                'type': q['type'],
                'answer': q['answer']
            }
        return None

    def check_answer(self, user_answer):
        current_q = self.get_current_question()
        if not current_q:
            return False

        user_answer_clean = user_answer.strip().lower()
        correct_answer = str(current_q['answer']).strip().lower()

        # Check for alternative answers (separated by /)
        if '/' in correct_answer:
            possible_answers = [ans.strip() for ans in correct_answer.split('/')]
            correct = user_answer_clean in possible_answers
        else:
            correct = user_answer_clean == correct_answer

        if correct:
            self.correct_answers += 1

        return correct

    def next_question(self):
        self.current_question_index += 1

    def has_more_questions(self):
        return self.current_question_index < len(self.selected_questions)

    def get_progress(self):
        return f"{self.current_question_index + 1}/{len(self.selected_questions)}"

    def is_task_complete(self):
        return (not self.has_more_questions() and
                self.correct_answers == len(self.selected_questions))

    def is_final_task(self):
        return self.task_number == 6

    def reset_task(self):
        self.setup_task()