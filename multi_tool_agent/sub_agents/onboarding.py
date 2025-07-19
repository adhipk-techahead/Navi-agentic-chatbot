from google.adk.agents import Agent
from multi_tool_agent.tools.state_management import (
    get_assessment_status, set_assessment_status, 
    get_assessment_progress, update_assessment_progress,
    set_current_step, get_current_step
)
from multi_tool_agent.tools.user_profile import (
    get_user_profile, update_user_profile, update_multiple_profile_fields,
    calculate_bmi, get_bmi_category, generate_welcome_message, get_profile_schema
)
from multi_tool_agent.tools.session_management import get_current_user_id, get_session_info
from multi_tool_agent.sub_agents.prompt import ONBOARDING_PROMPT
from multi_tool_agent.config import MODEL

onboarding_agent = Agent(
    name="onboarding_wizard",
    model=MODEL,
    description="Stepwise onboarding wizard for medical history collection.",
    instruction=ONBOARDING_PROMPT,
    tools=[
        get_assessment_status, set_assessment_status,
        get_assessment_progress, update_assessment_progress,
        set_current_step, get_current_step,
        get_user_profile, update_user_profile, update_multiple_profile_fields,
        calculate_bmi, get_bmi_category, generate_welcome_message, get_profile_schema,
        get_current_user_id, get_session_info
    ],
) 