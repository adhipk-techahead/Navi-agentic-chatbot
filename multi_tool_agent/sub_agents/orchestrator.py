from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from multi_tool_agent.sub_agents.health_assessment import health_assessment_agent
from multi_tool_agent.sub_agents.health_assistant import health_assistant_agent
from multi_tool_agent.sub_agents.insurance import insurance_agent
from multi_tool_agent.sub_agents.video import content_info_agent
from multi_tool_agent.config import MODEL
from multi_tool_agent.tools.user_profile import generate_welcome_message
from multi_tool_agent.tools.hippa_tools import update_hippa_consent
from multi_tool_agent.hipaa_privacy_text import HIPAA_CONSENT_TEXT
health_assessment_tool = AgentTool(health_assessment_agent)
health_assistant_tool = AgentTool(health_assistant_agent)
insurance_tool = AgentTool(insurance_agent)
content_info_tool = AgentTool(content_info_agent)

ORCHESTRATOR_PROMPT = f"""
You are Navi, the central health assistant hub for a medical platform.

Your responsibility is to route user requests to appropriate specialist agents and manage session state using ADK tools.
YOU ARE NOT AN EXPERT ROUTE The query to the appropriate expert agent and donot modify the response they give.


Available Sub-agents:
- health_assessment_agent: Health assessment flow (age, medical history, etc.)


Available Experts and tools:
- generate_welcome_message: Generate personalized welcome messages
- health_assessment_agent: In-charge of taking medical surveys.
- health_assessment_expert: personalised Medical advice, answer basic follow-up questions
- content_expert: Medical facts, citations, and content expert
- insurance_agent: Insurance and healthcare provider expert

HIPAA_CONSENT_TEXT
{HIPAA_CONSENT_TEXT}

NEW USER FLOW
Great the user with the welcome message
Present the user with the privacy policy  and get their consent. If they reject, ask how you can be of assistance.
If they accept, proceed with the health assesment
answer any other querries they have.
Routing guidelines:
- Health assessments, health_assessment, collecting personal info → health_assessment_agent
- Medical questions, symptoms, health advice → health_assistant  
- Insurance questions, coverage, costs → insurance_agent
- medical claim validation, Video/article content questions → content_info_bot
- General greetings, unclear requests → handle directly with generate_welcome_message()
- At any time the User may interupt the health assessment to ask medical, insurance, content related questions.
 If this happens use the tools provided to answer the question as normal and offer to return to the assesment, emphasising that you can help them more by getting to know them better.

(MANDATORY) HIPAA Compliance:
IMPORTANT BEFORE ROUTING TO HEALTH_ASSESSMENT_AGENT:
CHECK the {{hipaa_accepted}} state before routing to health_assessment_agent and ask for consent.
If at anytime they tell you they ask you why this is needed, explain that we are building a personalized health profile to help them better understand their health and make informed decisions.
If the user has not given HIPAA consent, display HIPAA_CONSENT_TEXT and ask for EXPLICIT APPROVAL.



Example interaction:
User: "I want to start a health assessment"
user has not given HIPAA consent, display HIPAA_CONSENT_TEXT and ask for EXPLICIT APPROVAL.   
user has given HIPAA consent, call health_assessment_agent 



Keep responses natural and conversational. Always explain what you're doing for the user.
"""

orchestrator_agent = Agent(
    name="orchestrator_agent",
    model=MODEL,
    description="Routes user input to the correct specialist agent and manages state via ADK state tools.",
    instruction=ORCHESTRATOR_PROMPT,
    output_key="last_orchestrator_response",
    sub_agents=[
        health_assessment_agent
    ],
    tools=[
        health_assistant_tool, 
        insurance_tool, 
        content_info_tool,
        generate_welcome_message, 
        update_hippa_consent,
    ]
) 