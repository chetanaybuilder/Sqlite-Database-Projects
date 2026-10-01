"""Pytest suite for sqlite projects using in-memory databases."""

import pytest

from src.sqlite_projects.auth.service import AuthService
from src.sqlite_projects.chatbot.history import ChatHistory
from src.sqlite_projects.db import initialize_schema
from src.sqlite_projects.student_db.models import Student
from src.sqlite_projects.student_db.repository import StudentRepository


@pytest.fixture
def memory_db():
    """Provides an in-memory SQLite database path for testing."""
    db_path = ":memory:"
    # Initialize the schema on the in-memory database
    # In SQLite, :memory: creates a new DB for each connection.
    # To test properly across functions we use a file-based temporary db.
    return db_path


@pytest.fixture
def temp_db(tmp_path):
    """Provides a temporary file-based SQLite database for testing."""
    db_path = str(tmp_path / "test.db")
    initialize_schema(db_path)
    return db_path


def test_student_repository(temp_db):
    """Test adding and retrieving students."""
    repo = StudentRepository(db_path=temp_db)

    # Add student
    student = Student(name="John Doe", age=20)
    added = repo.add_student(student)

    assert added.id is not None
    assert added.name == "John Doe"

    # Retrieve all
    all_students = repo.get_all_students()
    assert len(all_students) == 1
    assert all_students[0].name == "John Doe"


def test_auth_service(temp_db):
    """Test registration and login flow with bcrypt."""
    auth = AuthService(db_path=temp_db)

    # Register
    success = auth.register("testuser", "test@test.com", "password123")
    assert success is True

    # Duplicate email register should fail
    duplicate = auth.register("testuser2", "test@test.com", "password456")
    assert duplicate is False

    # Login success
    user = auth.login("test@test.com", "password123")
    assert user is not None
    assert user["username"] == "testuser"

    # Login failure (wrong password)
    failed = auth.login("test@test.com", "wrongpass")
    assert failed is None


def test_chat_history(temp_db):
    """Test saving and retrieving chat messages."""
    history = ChatHistory(db_path=temp_db)

    history.save_message("Hello AI", "Hello Human")

    msgs = history.get_history()
    assert len(msgs) == 1
    assert msgs[0]["user"] == "Hello AI"
    assert msgs[0]["bot"] == "Hello Human"
