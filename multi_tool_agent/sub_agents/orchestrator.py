from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from multi_tool_agent.sub_agents.onboarding import onboarding_agent
from multi_tool_agent.sub_agents.health_assistant import health_assistant_agent
from multi_tool_agent.sub_agents.insurance import insurance_agent
from multi_tool_agent.sub_agents.video import content_info_agent
from multi_tool_agent.sub_agents.prompt import ORCHESTRATOR_PROMPT
from multi_tool_agent.tools.state_management import (
    get_user_state, get_assessment_status, get_screen_context,
    set_assessment_status, set_screen_context
)
from multi_tool_agent.tools.user_profile import (
    get_user_profile, generate_welcome_message, get_profile_completion_percentage
)
from multi_tool_agent.tools.session_management import get_current_user_id, get_session_info
from multi_tool_agent.config import MODEL

onboarding_tool = AgentTool(onboarding_agent)
health_assistant_tool = AgentTool(health_assistant_agent)
insurance_tool = AgentTool(insurance_agent)
content_info_tool = AgentTool(content_info_agent)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    model=MODEL,
    description="Routes user input to the correct specialist agent (onboarding, health assistant, insurance, content info) as a tool.",
    instruction=ORCHESTRATOR_PROMPT,
    tools=[
        onboarding_tool, health_assistant_tool, insurance_tool, content_info_tool,
        get_user_state, get_assessment_status, get_screen_context,
        set_assessment_status, set_screen_context,
        get_user_profile, generate_welcome_message, get_profile_completion_percentage,
        get_current_user_id, get_session_info
    ],
) 