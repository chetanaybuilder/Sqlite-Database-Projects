"""Chat history management in SQLite."""

import logging
from typing import Dict, List

from src.sqlite_projects.db import get_db_connection

logger = logging.getLogger(__name__)


class ChatHistory:
    """Manages storing and retrieving chat messages."""

    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path

    def save_message(self, user_message: str, bot_response: str) -> None:
        """Save a user message and bot response to the database."""
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO messages (user_message, bot_response) VALUES (?, ?)",
                (user_message, bot_response),
            )
            logger.info("Chat message saved.")

    def get_history(self) -> List[Dict[str, str]]:
        """Retrieve the entire chat history."""
        with get_db_connection(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT user_message, bot_response FROM messages ORDER BY id"
            )
            rows = cursor.fetchall()
            return [
                {"user": row["user_message"], "bot": row["bot_response"]}
                for row in rows
            ]
