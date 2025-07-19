from google.adk.agents import Agent
from multi_tool_agent.tools.state_management import (
    get_assessment_status, get_assessment_progress, update_assessment_progress
)
from multi_tool_agent.sub_agents.prompt import HEALTH_ASSISTANT_PROMPT
from multi_tool_agent.config import MODEL

health_assistant_agent = Agent(
    name="health_assistant",
    model=MODEL,
    description="Provides empathetic medical guidance, follow-up questions, and basic non-medical diagnosis.",
    instruction=HEALTH_ASSISTANT_PROMPT,
    tools=[
        get_assessment_status, get_assessment_progress, update_assessment_progress
    ],
) 