import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from autogen_agentchat.agents import AssistantAgent
from models.openAIModel import openai_model_client

planner_agent = AssistantAgent(
    "planner_agent",
    model_client=openai_model_client,
    description="A helpful assistant that can plan trips.",
    system_message="You are a helpful assistant that can suggest a travel plan for a user based on their request.",
)