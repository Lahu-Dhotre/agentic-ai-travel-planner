import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_app.agent.planner_agent import planner_agent
from autogen_app.agent.local_agent import local_agent
from autogen_app.agent.travel_summary_agent import travel_summary_agent
from config.settings import MAX_TURNS, TERMINATION_WORDS



# Modular, enterprise-standard wrapper class for the travel team
class TravelTeamService:
    def __init__(self):
        self.team = RoundRobinGroupChat(
            [planner_agent, local_agent, travel_summary_agent],
            termination_condition=MaxMessageTermination(max_messages=MAX_TURNS)
        )

    async def plan_trip(self, params: dict) -> list:
        """
        Accepts a dictionary of trip parameters and returns an itinerary as a list of strings.
        """
        # Build a prompt from structured input
        destination = params.get("destination", "an unknown destination")
        start_date = params.get("start_date", "an unknown start date")
        end_date = params.get("end_date", "an unknown end date")
        travelers = params.get("travelers")
        preferences = params.get("preferences")

        prompt = f"Plan a trip to {destination} from {start_date} to {end_date}."
        if travelers:
            prompt += f" Number of travelers: {travelers}."
        if preferences:
            prompt += f" Preferences: {preferences}."

        # Pass the prompt as the initial user message to the team
        response = await self.team.run([{"role": "user", "content": prompt}])
        # Normalize response to a list of strings (extract 'content' if present)
        if hasattr(response, 'messages'):
            itinerary = [getattr(msg, 'content', str(msg)) for msg in response.messages]
        elif isinstance(response, list):
            itinerary = [getattr(item, 'content', str(item)) for item in response]
        elif isinstance(response, str):
            itinerary = [line.strip() for line in response.split('\n') if line.strip()]
        else:
            itinerary = [str(response)]
        return itinerary

# Singleton instance for use in FastAPI and elsewhere
travel_team_service = TravelTeamService()