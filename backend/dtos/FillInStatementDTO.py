# backend/dto/FillInStatementDTO.py
from dataclasses import dataclass
from typing import List

@dataclass
class FillInStatementDTO:
    id: int
    text_segments: List[str]
    answers: List[str]
