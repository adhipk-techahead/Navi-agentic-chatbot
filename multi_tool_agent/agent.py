
from __future__ import annotations
from google.adk.agents import Agent
from .sub_agents.orchestrator import orchestrator_agent
from .sub_agents.onboarding import onboarding_agent
from .sub_agents.insurance import insurance_agent
from .sub_agents.video import video_info_agent

# This variable is required for ADK agent discovery
root_agent = Agent(
    name="root_health_agent",
    model="gemini-2.0-flash",
    description="Root agent for multi-agent health chatbot. Orchestrates onboarding, insurance, and video info agents.",
    instruction="You are the root agent. Route user queries to the correct specialist agent via the orchestrator.",
    sub_agents=[orchestrator_agent, onboarding_agent, insurance_agent, video_info_agent],
)