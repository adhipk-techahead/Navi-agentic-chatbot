from __future__ import annotations
from typing import AsyncGenerator
from typing_extensions import override
from google.adk.agents import BaseAgent, LlmAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from .sub_agents.orchestrator import orchestrator_agent
import re
import json

class SessionInitializerAgent(BaseAgent):
    """
    Custom agent that initializes session state and orchestrates the main workflow.
    
    This agent's only job is to:
    1. Initialize all required session state variables 
    2. Call the orchestrator agent to handle user requests
    3. Monitor orchestrator responses and update state accordingly
    """
    
    # Field declarations for Pydantic
    orchestrator: LlmAgent
    
    # Allow arbitrary types for Pydantic
    model_config = {"arbitrary_types_allowed": True}
    
    def __init__(self, name: str = "SessionInitializerAgent"):
        """Initialize the session initializer agent with the orchestrator."""
        super().__init__(
            name=name,
            orchestrator=orchestrator_agent,
            sub_agents=[orchestrator_agent]
        )
    
    @override
    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        """
        Initialize session state and run the orchestrator agent.
        
        Args:
            ctx: InvocationContext with access to session.state
            
        Yields:
            Events from the orchestrator agent
        """
        # Initialize session state if not already present
        await self._initialize_session_state(ctx)
        
        # Run the orchestrator agent and monitor its responses
        async for event in self.orchestrator.run_async(ctx):
            # Monitor responses and update state accordingly
            await self._update_state_from_event(ctx, event)
            yield event
    
    async def _initialize_session_state(self, ctx: InvocationContext) -> None:
        """Initialize all required session state variables."""
        
        # HIPAA Compliance State
        if 'hipaa_accepted' not in ctx.session.state:
            ctx.session.state['hipaa_accepted'] = False
        
        # Health Assessment State
        if 'health_assessment' not in ctx.session.state:
            ctx.session.state['health_assessment'] = {}
        
        if 'last_assesment_question' not in ctx.session.state:
            ctx.session.state['last_assesment_question'] = None
        
        # Assessment Flow State
        if 'assessment_status' not in ctx.session.state:
            ctx.session.state['assessment_status'] = 'not_started'  # 'not_started', 'ongoing', 'completed'
        
        if 'screen' not in ctx.session.state:
            ctx.session.state['screen'] = 'chat_interface'  # 'chat_interface', 'content_page', 'insurance'
        
        if 'current_step' not in ctx.session.state:
            ctx.session.state['current_step'] = None
        
        if 'assessment_progress' not in ctx.session.state:
            ctx.session.state['assessment_progress'] = {}
        
        # User Profile State (using user: prefix for persistence)
        user_profile_fields = [
            'user:name', 'user:age', 'user:gender', 'user:demographics',
            'user:height', 'user:weight', 'user:bmi', 'user:bmi_category',
            'user:occupation', 'user:lifestyle_score', 'user:exercise_frequency',
            'user:smoking', 'user:drinking', 'user:diet', 'user:allergies',
            'user:stress_level', 'user:family_history', 'user:pre_existing_conditions',
            'user:current_medications', 'user:profile_completed'
        ]
        
        for field in user_profile_fields:
            if field not in ctx.session.state:
                ctx.session.state[field] = ""
        
        # Response Tracking (for agent outputs)
        if 'last_orchestrator_response' not in ctx.session.state:
            ctx.session.state['last_orchestrator_response'] = ""
        
        if 'last_health_response' not in ctx.session.state:
            ctx.session.state['last_health_response'] = ""

    async def _update_state_from_event(self, ctx: InvocationContext, event: Event) -> None:
        """Monitor events and update state based on content."""
        
        # Only process events with text content
        if not event.content or not event.content.parts:
            return
            
        response_text = ""
        for part in event.content.parts:
            if part.text:
                response_text += part.text
        
        if not response_text:
            return
            
        response_lower = response_text.lower()
        
        # Update last orchestrator response
        ctx.session.state['last_orchestrator_response'] = response_text
        
        # Check for HIPAA consent in the conversation
        if any(phrase in response_lower for phrase in ["yes, i consent", "i consent", "i agree to proceed"]):
            ctx.session.state['hipaa_accepted'] = True
            
        # Check for HIPAA consent tool calls
        if "hipaa consent updated to: true" in response_lower:
            ctx.session.state['hipaa_accepted'] = True
        elif "hipaa consent updated to: false" in response_lower:
            ctx.session.state['hipaa_accepted'] = False
        
        # Extract user information from responses
        await self._extract_user_data(ctx, response_lower)
        
        # Update assessment status if health assessment is mentioned
        if any(phrase in response_lower for phrase in ["health assessment", "start assessment", "begin assessment"]):
            if ctx.session.state['assessment_status'] == 'not_started':
                ctx.session.state['assessment_status'] = 'ongoing'

    async def _extract_user_data(self, ctx: InvocationContext, response_text: str) -> None:
        """Extract user data from response text using pattern matching."""
        
        # Extract age
        age_patterns = [
            r"i'm (\d+) years old",
            r"i am (\d+) years old", 
            r"(\d+) years old",
            r"my age is (\d+)"
        ]
        for pattern in age_patterns:
            match = re.search(pattern, response_text)
            if match:
                age = match.group(1)
                if 1 <= int(age) <= 120:
                    ctx.session.state['user:age'] = age
                break
        
        # Extract gender
        gender_patterns = [
            (r"i'm (male|female)", 1),
            (r"i am (male|female)", 1),
            (r"identify as (male|female|other)", 1),
            (r"(male|female|other)", 1)
        ]
        if "prefer not to say" in response_text:
            ctx.session.state['user:gender'] = 'prefer_not_to_say'
        else:
            for pattern, group in gender_patterns:
                match = re.search(pattern, response_text)
                if match:
                    gender = match.group(group)
                    ctx.session.state['user:gender'] = gender
                    break
        
        # Extract symptoms
        symptom_keywords = ["headache", "pain", "hurt", "ache", "fever", "cough", "nausea", "dizzy", "tired"]
        found_symptoms = [keyword for keyword in symptom_keywords if keyword in response_text]
        if found_symptoms:
            existing_symptoms = ctx.session.state.get('user:symptoms', "")
            new_symptoms = ", ".join(found_symptoms)
            if existing_symptoms:
                ctx.session.state['user:symptoms'] = f"{existing_symptoms}, {new_symptoms}"
            else:
                ctx.session.state['user:symptoms'] = new_symptoms

# Create the root agent instance
root_agent = SessionInitializerAgent()