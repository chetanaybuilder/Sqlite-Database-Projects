"""CLI for the authentication service."""

import argparse
import logging

from src.sqlite_projects.auth.service import AuthService
from src.sqlite_projects.db import initialize_schema

logger = logging.getLogger(__name__)


def setup_parser() -> argparse.ArgumentParser:
    """Setup argument parser for auth CLI."""
    parser = argparse.ArgumentParser(description="Authentication CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Register command
    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("username", help="Username")
    register_parser.add_argument("email", help="Email address")
    register_parser.add_argument("password", help="Password")

    # Login command
    login_parser = subparsers.add_parser("login", help="Login to an account")
    login_parser.add_argument("email", help="Email address")
    login_parser.add_argument("password", help="Password")

    return parser


def main() -> None:
    """Main entrypoint for auth CLI."""
    logging.basicConfig(level=logging.INFO)
    initialize_schema()

    parser = setup_parser()
    args = parser.parse_args()

    auth_service = AuthService()

    if args.command == "register":
        success = auth_service.register(args.username, args.email, args.password)
        if success:
            print("Registration successful!")
        else:
            print("Registration failed. Email might already exist.")

    elif args.command == "login":
        user = auth_service.login(args.email, args.password)
        if user:
            print(f"Login successful! Welcome {user['username']}.")
        else:
            print("Invalid email or password.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
