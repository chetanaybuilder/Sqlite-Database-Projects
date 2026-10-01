"""CLI for the student database."""

import argparse
import logging

from src.sqlite_projects.db import initialize_schema
from src.sqlite_projects.student_db.models import Student
from src.sqlite_projects.student_db.repository import StudentRepository

logger = logging.getLogger(__name__)


def setup_parser() -> argparse.ArgumentParser:
    """Setup argument parser for student CLI."""
    parser = argparse.ArgumentParser(description="Student Database CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new student")
    add_parser.add_argument("name", help="Student's name")
    add_parser.add_argument("age", type=int, help="Student's age")

    # List command
    subparsers.add_parser("list", help="List all students")

    return parser


def main() -> None:
    """Main entrypoint for student CLI."""
    logging.basicConfig(level=logging.INFO)
    initialize_schema()

    parser = setup_parser()
    args = parser.parse_args()

    repo = StudentRepository()

    if args.command == "add":
        student = Student(name=args.name, age=args.age)
        repo.add_student(student)
        print(f"Added: {student}")
    elif args.command == "list":
        students = repo.get_all_students()
        for s in students:
            print(f"[{s.id}] {s.name}, Age: {s.age}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
