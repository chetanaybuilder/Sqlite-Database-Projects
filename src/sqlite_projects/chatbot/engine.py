"""Chatbot response logic using Google GenAI."""

import logging
import os
from typing import Optional

from google import genai

logger = logging.getLogger(__name__)


class ChatbotEngine:
    """Handles generating responses using the Google GenAI API."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.warning("GEMINI_API_KEY not found. Responses will fail.")
            self.client = None
        else:
            self.client = genai.Client(api_key=self.api_key)

    def generate_response(self, user_message: str) -> str:
        """Generate a response following strict Chetanay AI rules."""
        if not self.client:
            return "API Key missing. Cannot generate response."

        prompt = f"""You are Chetanay AI.
Rules:
- Answer in this exact format.
- Start with a relevant emoji.
- Use 2-5 relevant emojis naturally.
- Keep answers under 100 words.
- Never use Markdown.
- Never use ***, **, or *.
- Never write long paragraphs.
- Use a short title.
- Then give 3-5 numbered points.
- Each point must be one short sentence.
- End with a one-line summary.

User Message: {user_message}"""

        try:
            result = self.client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt
            )
            return getattr(result, "text", None) or str(result)
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return "Sorry, I encountered an error generating a response."
