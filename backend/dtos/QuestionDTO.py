# backend/dto/QuestionDTO.py
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class QuestionDTO:
    id: int
    text: str
    # For questions coming from your Question entity we keep the answers as a list of tuples
    # where each tuple is (answer_text, is_correct_bool)
    answers: List[Tuple[str, bool]]
