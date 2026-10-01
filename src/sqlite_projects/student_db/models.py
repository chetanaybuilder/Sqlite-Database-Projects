"""Models for the student database."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    """Represents a student record."""

    name: str
    age: int
    id: Optional[int] = None
