from google.adk.agents import Agent
from multi_tool_agent.tools.insurance_api import get_insurance_record
from multi_tool_agent.sub_agents.prompt import INSURANCE_PROMPT
from multi_tool_agent.config import MODEL

insurance_agent = Agent(
    name="insurance_info_bot",
    model=MODEL,
    description="Answers insurance-related questions using user policy data.",
    instruction=INSURANCE_PROMPT,
    tools=[get_insurance_record],
) 