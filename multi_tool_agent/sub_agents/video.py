from google.adk.agents import Agent
from multi_tool_agent.tools.vector_db import query_vector_db, get_user_medical_preferences
from multi_tool_agent.sub_agents.prompt import CONTENT_INFO_PROMPT
from multi_tool_agent.config import MODEL

content_info_agent = Agent(
    name="content_info_bot",
    model=MODEL,
    description="Answers questions about medical videos/articles using validated claims and citations from vectorDB.",
    instruction=CONTENT_INFO_PROMPT,
    tools=[query_vector_db, get_user_medical_preferences],
) 