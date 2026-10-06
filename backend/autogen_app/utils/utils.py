import sys
import json

from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config.settings import TEXT_MENTION_TERMINATION

# Export for easy access
text_mention_termination = TEXT_MENTION_TERMINATION

def save_state(agent, filename):
    """Saves the state of an agent to a JSON file."""
    state = {
        "name": agent.name,
        "description": agent.description,
        "system_message": agent.system_message,
        "conversation_history": agent.get_conversation_history(),
    }
    with open(filename, 'w') as f:
        json.dump(state, f, indent=4)
        
def load_state(agent, filename):
    """Loads the state of an agent from a JSON file."""
    with open(filename, 'r') as f:
        state = json.load(f)
    agent.name = state.get("name", "")
    agent.description = state.get("description", "")
    agent.system_message = state.get("system_message", "")
    agent.set_conversation_history(state.get("conversation_history", []))