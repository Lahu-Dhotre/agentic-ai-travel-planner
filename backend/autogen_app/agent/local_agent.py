import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from autogen_agentchat.agents import AssistantAgent
from models.openAIModel import openai_model_client

local_agent = AssistantAgent(
    "local_agent",
    model_client=openai_model_client,
    description="A local assistant that can suggest local activities or places to visit.",
    system_message="You are a helpful assistant that can suggest authentic and interesting local activities or places to visit for a user and can utilize any context information provided.",
)