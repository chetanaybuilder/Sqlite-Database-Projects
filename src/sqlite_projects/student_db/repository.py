"""CRUD operations for students."""

import logging
from typing import List, Optional

from src.sqlite_projects.db import get_db_connection
from src.sqlite_projects.student_db.models import Student

logger = logging.getLogger(__name__)


class StudentRepository:
    """Repository for managing student records in the database."""

    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path

    def add_student(self, student: Student) -> Student:
        """Add a new student to the database using parameterized queries."""
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, age) VALUES (?, ?)",
                (student.name, student.age),
            )
            student.id = cursor.lastrowid
            logger.info(f"Added student: {student.name}")
            return student

    def get_all_students(self) -> List[Student]:
        """Retrieve all students from the database."""
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, age FROM students")
            rows = cursor.fetchall()
            return [
                Student(id=row["id"], name=row["name"], age=row["age"]) for row in rows
            ]

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """Retrieve a student by their ID."""
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, age FROM students WHERE id = ?", (student_id,)
            )
            row = cursor.fetchone()
            if row:
                return Student(id=row["id"], name=row["name"], age=row["age"])
            return None
