"""Authentication service handling registration and login securely."""

import logging
import sqlite3
from typing import Dict, Optional

import bcrypt

from src.sqlite_projects.db import get_db_connection

logger = logging.getLogger(__name__)


class AuthService:
    """Service for securely registering and authenticating users."""

    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path

    def register(self, username: str, email: str, password: str) -> bool:
        """
        Register a new user with a hashed password.

        Returns:
            True if registration was successful, False if email exists.
        """
        # Hash the password securely with bcrypt
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                    (username, email, password_hash),
                )
                logger.info(f"User {username} registered successfully.")
                return True
            except sqlite3.IntegrityError:
                logger.warning(f"Registration failed: Email {email} already exists.")
                return False

    def login(self, email: str, password: str) -> Optional[Dict[str, str]]:
        """
        Authenticate a user by verifying their password hash.

        Returns:
            A dictionary with user details if successful, None otherwise.
        """
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, username, password_hash FROM users WHERE email = ?",
                (email,),
            )
            row = cursor.fetchone()

            if row:
                stored_hash = row["password_hash"].encode("utf-8")
                # Verify password
                if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
                    logger.info(f"User {row['username']} logged in successfully.")
                    return {
                        "id": row["id"],
                        "username": row["username"],
                        "email": email,
                    }

            logger.warning(f"Failed login attempt for email {email}.")
            return None
