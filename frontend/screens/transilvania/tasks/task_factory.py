from .task_screen_base import TaskScreenBase
from frontend.regions.transilvania.colors import TASK_BG_COLORS
from frontend.regions.transilvania.tasks.task_data import (
    TASK_1_QUESTIONS, TASK_2_QUESTIONS, TASK_3_QUESTIONS, TASK_4_QUESTIONS
)


TASK_CONFIG = {
    1: {'questions': TASK_1_QUESTIONS, 'color': TASK_BG_COLORS['task_1']},
    2: {'questions': TASK_2_QUESTIONS, 'color': TASK_BG_COLORS['task_2']},
    3: {'questions': TASK_3_QUESTIONS, 'color': TASK_BG_COLORS['task_3']},
    4: {'questions': TASK_4_QUESTIONS, 'color': TASK_BG_COLORS['task_4']},
}


def create_task_screen(task_number):
    if task_number not in TASK_CONFIG:
        raise ValueError(f"Invalid task number: {task_number}")

    config = TASK_CONFIG[task_number]
    return TaskScreenBase(
        questions=config['questions'],
        bg_color=config['color'],
        task_number=task_number,
        name=f'task_{task_number}'
    )

