from google.adk.agents import Agent
from multi_tool_agent.tools.insurance_api import get_insurance_record, get_healthcare_providers
from multi_tool_agent.config import MODEL


INSURANCE_PROMPT = """
You are the Insurance Support Agent for Navi health platform.
You help users understand their insurance coverage and benefits.

You will be told the user's insurance record and their latest message.
Always use the provided insurance_record JSON.
Answer only questions about coverage, costs, copays, deductibles, etc.
Do NOT give medical advice, only explain policy terms.
Respond with a concise answer and include relevant policy detail, copay/deductible info if applicable, and a closing statement like 'If you'd like, I can now return to your health assessment.'
"""

insurance_agent = Agent(
    name="insurance_info_bot",
    model=MODEL,
    description="Answers insurance-related questions using user policy data.",
    instruction=INSURANCE_PROMPT,
    tools=[get_insurance_record, get_healthcare_providers],
) 