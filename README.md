# Professional SQLite Database Projects 💾

> A portfolio-grade Python suite demonstrating secure database management, authentication, and AI chatbot integration using SQLite.

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![CI Status](https://github.com/chetanaybuilder/Sqlite-Database-Projects/actions/workflows/ci.yml/badge.svg)

## 📌 Overview
This repository contains three refactored, production-ready projects centered around SQLite. What started as beginner scripts has been re-architected into a cohesive, secure, and professional Python package utilizing OOP, parameterized queries, dependency injection, and modern cryptography.

## ✨ Features
- **Student Database**: A CRUD application utilizing the Repository pattern and Dataclasses.
- **Secure Authentication**: Registration and login mechanisms secured with `bcrypt` password hashing (no plaintext passwords!).
- **AI Chatbot**: Contextual AI chatbot integrated with `google-genai`, storing conversational history persistently in SQLite.
- **Security-First**: Strictly uses parameterized queries to prevent SQL injection. Secrets are safely loaded via `.env`.

## 🛠️ Tech Stack
- **Language**: Python 3.9+
- **Database**: SQLite3
- **Security**: `bcrypt`
- **AI**: `google-genai`
- **Tooling**: `pytest`, `black`, `ruff`

## 📂 Architecture
```
Sqlite-Database-Projects/
├── src/sqlite_projects/
│   ├── __init__.py
│   ├── db.py                 # Connection manager, Contexts, Migrations
│   ├── student_db/           # Student CRUD domain
│   │   ├── models.py         # Dataclasses
│   │   ├── repository.py     # Data access layer
│   │   └── cli.py            # Student command line interface
│   ├── chatbot/              # AI Chat domain
│   │   ├── engine.py         # Gemini API generation logic
│   │   ├── history.py        # SQLite history management
│   │   └── cli.py            # Chatbot command line interface
│   └── auth/                 # Authentication domain
│       ├── service.py        # Registration, Login, bcrypt hashing
│       └── cli.py            # Auth command line interface
├── tests/                    # Pytest suite using in-memory SQLite (:memory:)
├── pyproject.toml            # Project packaging and metadata
├── requirements.txt          # Dependencies
├── .env.example              # Secret structure
└── README.md                 # Documentation
```

## 🚀 Installation & Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chetanaybuilder/Sqlite-Database-Projects.git
   cd Sqlite-Database-Projects
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**
   ```bash
   cp .env.example .env
   # Add your Gemini API key to .env if you wish to use the chatbot
   ```

## 💻 CLI Usage Examples

**1. Student Database:**
```bash
python -m src.sqlite_projects.student_db.cli add "Chetanay" 16
python -m src.sqlite_projects.student_db.cli list
```
*Output:*
```
Added student: Chetanay
[1] Chetanay, Age: 16
```

**2. Secure Authentication:**
```bash
python -m src.sqlite_projects.auth.cli register user1 "user@example.com" "securepass123"
python -m src.sqlite_projects.auth.cli login "user@example.com" "securepass123"
```
*Output:*
```
Registration successful!
Login successful! Welcome user1.
```

**3. AI Chatbot:**
```bash
python -m src.sqlite_projects.chatbot.cli "Tell me about Python."
python -m src.sqlite_projects.chatbot.cli --history
```

## 🧪 Testing
The project uses `pytest` and runs tests against completely isolated, in-memory SQLite databases (`:memory:`), ensuring no leftover test artifacts.

```bash
# Install testing dependencies
pip install -e .[dev]

# Run tests
pytest
```

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! 

## 🧑‍💻 Author
**Chetanay Batra** - [@chetanaybuilder](https://github.com/chetanaybuilder)

## 📄 License
This project is [MIT](LICENSE) licensed.
