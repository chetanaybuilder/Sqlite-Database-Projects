"""CLI for interacting with the chatbot."""

import argparse
import logging

from dotenv import load_dotenv

from src.sqlite_projects.chatbot.engine import ChatbotEngine
from src.sqlite_projects.chatbot.history import ChatHistory
from src.sqlite_projects.db import initialize_schema

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entrypoint for chatbot CLI."""
    load_dotenv()
    logging.basicConfig(level=logging.INFO)
    initialize_schema()

    parser = argparse.ArgumentParser(description="Chatbot CLI")
    parser.add_argument("message", nargs="?", help="Message to send to the chatbot")
    parser.add_argument("--history", action="store_true", help="Show chat history")

    args = parser.parse_args()

    history_manager = ChatHistory()

    if args.history:
        history = history_manager.get_history()
        for msg in history:
            print(f"You: {msg['user']}\nBot: {msg['bot']}\n")
        return

    if not args.message:
        parser.print_help()
        return

    engine = ChatbotEngine()
    print("Generating response...")
    response = engine.generate_response(args.message)
    print(f"\nBot: {response}\n")

    history_manager.save_message(args.message, response)


if __name__ == "__main__":
    main()
