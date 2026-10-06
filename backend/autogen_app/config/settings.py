import os
from dotenv import load_dotenv
from pathlib import Path
from autogen_agentchat.conditions import TextMentionTermination

# Load environment variables from .env file (explicit path)
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')  # Standard OpenAI API key name
print(f"[DEBUG] Loaded OPENAI_API_KEY: {'SET' if OPENAI_API_KEY else 'NOT SET'}")
MODEL = 'gpt-4o-mini'
MAX_TURNS = 5
TERMINATION_WORDS = ['goodbye', 'exit', 'quit', 'stop']
TEMPERATURE = 0.7

# Create combined termination condition for any of the termination words
TEXT_MENTION_TERMINATION = (
    TextMentionTermination("goodbye") |
    TextMentionTermination("exit") |
    TextMentionTermination("quit") |
    TextMentionTermination("stop")
)