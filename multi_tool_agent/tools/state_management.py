# In-memory state management (replace with Redis/DynamoDB in production)
from typing import Optional
from multi_tool_agent.tools.session_management import get_current_user_id

user_states =  {
    "user_123":{
        "assessment_status": "not_started",
        "screen": "chat_interface",
        "assessment_progress": {},
        "current_step": None,
        "last_activity": None
    }
}

def get_user_state(user_id: Optional[str] = None) -> dict:
    """Get complete user state including assessment status and screen context. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    return user_states.get(user_id, {
        "assessment_status": "not_started",
        "screen": "chat_interface",
        "assessment_progress": {},
        "current_step": None,
        "last_activity": None
    })

def set_assessment_status(status: str, user_id: Optional[str] = None) -> bool:
    """Set assessment status: 'not_started', 'ongoing', 'completed'. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    if status not in ["not_started", "ongoing", "completed"]:
        return False
    
    if user_id not in user_states:
        user_states[user_id] = {}
    
    user_states[user_id]["assessment_status"] = status
    user_states[user_id]["last_activity"] = "assessment_status_update"
    return True

def get_assessment_status(user_id: Optional[str] = None) -> str:
    """Get current assessment status for user. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    return get_user_state(user_id)["assessment_status"]

def set_screen_context(screen: str, user_id: Optional[str] = None) -> bool:
    """Set current screen context: 'chat_interface', 'content_page', 'insurance', etc. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    if user_id not in user_states:
        user_states[user_id] = {}
    
    user_states[user_id]["screen"] = screen
    user_states[user_id]["last_activity"] = "screen_change"
    return True

def get_screen_context(user_id: Optional[str] = None) -> str:
    """Get current screen context for user. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    return get_user_state(user_id)["screen"]

def update_assessment_progress(step: str, data: dict, user_id: Optional[str] = None) -> bool:
    """Update assessment progress with step data. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    if user_id not in user_states:
        user_states[user_id] = {}
    
    if "assessment_progress" not in user_states[user_id]:
        user_states[user_id]["assessment_progress"] = {}
    
    user_states[user_id]["assessment_progress"][step] = data
    user_states[user_id]["current_step"] = step
    user_states[user_id]["last_activity"] = "assessment_progress_update"
    return True

def get_assessment_progress(user_id: Optional[str] = None) -> dict:
    """Get current assessment progress for user. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    return get_user_state(user_id)["assessment_progress"]

def set_current_step(step: str, user_id: Optional[str] = None) -> bool:
    """Set current assessment step. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    if user_id not in user_states:
        user_states[user_id] = {}
    
    user_states[user_id]["current_step"] = step
    user_states[user_id]["last_activity"] = "step_change"
    return True

def get_current_step(user_id: Optional[str] = None) -> str:
    """Get current assessment step for user. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    return get_user_state(user_id)["current_step"]

def reset_user_state(user_id: Optional[str] = None) -> bool:
    """Reset user state to initial values. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    user_states[user_id] = {
        "assessment_status": "not_started",
        "screen": "chat_interface",
        "assessment_progress": {},
        "current_step": None,
        "last_activity": "reset"
    }
    return True

def get_all_user_states() -> dict:
    """Get all user states (for debugging/admin purposes)."""
    return user_states 