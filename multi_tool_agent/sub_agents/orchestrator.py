from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from multi_tool_agent.sub_agents.onboarding import onboarding_agent
from multi_tool_agent.sub_agents.insurance import insurance_agent
from multi_tool_agent.sub_agents.video import video_info_agent

onboarding_tool = AgentTool(onboarding_agent)
insurance_tool = AgentTool(insurance_agent)
video_tool = AgentTool(video_info_agent)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    model="gemini-2.0-flash",
    description="Routes user input to the correct specialist agent (onboarding, insurance, video) as a tool.",
    instruction=(
        "You are the Orchestrator in a multi-agent health chatbot.\n"
        "You will be told the current state (e.g., 'onboarding_wizard', step 4) and the user's message.\n"
        "Your job is to decide which specialist agent (onboarding, insurance, or video) should handle the user's message.\n"
        "Call the appropriate agent as a tool with the user's message and any relevant context.\n"
        "Maintain context and ensure seamless routing between agents.\n"
        "Do not return an intent string. Instead, invoke the correct agent as a tool and return its response."
    ),
    tools=[onboarding_tool, insurance_tool, video_tool],
) 