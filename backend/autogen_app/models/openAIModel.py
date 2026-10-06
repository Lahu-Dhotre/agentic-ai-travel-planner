import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.settings import OPENAI_API_KEY, MODEL, MAX_TURNS, TERMINATION_WORDS, TEMPERATURE
from autogen_ext.models.openai import OpenAIChatCompletionClient

openai_model_client = OpenAIChatCompletionClient(
    model=MODEL,
    api_key=OPENAI_API_KEY,
    temperature=TEMPERATURE
)