from google.adk.agents import Agent
from multi_tool_agent.tools.mock_user_db import get_onboarding_progress, update_onboarding_progress

onboarding_agent = Agent(
    name="onboarding_wizard",
    model="gemini-2.0-flash",
    description="Stepwise onboarding wizard for medical history collection.",
    instruction=(
        "You are the Onboarding Wizard for a medical chatbot.\n"
        "You will be told the user's onboarding progress and their latest message.\n"
        "Your goal: step-by-step collection of: Age, Gender, Height, Weight, Allergies, Existing Conditions, Current Medications.\n"
        "If the user provides requested info, store it and ask the next question.\n"
        "If the user asks something else (insurance/video), indicate interruption: 'INTERRUPT'.\n"
        "Otherwise, ask the next onboarding question.\n"
        "Output a JSON object with: status ('RESPOND' | 'INTERRUPT' | 'COMPLETED'), message, onboarding_progress."
    ),
    tools=[get_onboarding_progress, update_onboarding_progress],
) 