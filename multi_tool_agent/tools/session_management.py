# Session management with dynamic user ID support
# In production, this would integrate with your authentication/session system

# Default user ID (fallback)
DEFAULT_USER_ID = "user_123"

# Current session user ID (can be set dynamically)
_current_user_id = None

def set_current_user_id(user_id: str) -> None:
    """Set the current user ID for this session."""
    global _current_user_id
    _current_user_id = user_id

def get_current_user_id() -> str:
    """Get the current user ID from session. Falls back to default if not set."""
    global _current_user_id
    if _current_user_id is None:
        return DEFAULT_USER_ID
    return _current_user_id

def get_session_info() -> dict:
    """Get current session information."""
    return {
        "user_id": get_current_user_id(),
        "session_active": True,
        "session_started": "now",
        "is_default_user": _current_user_id is None
    }

def clear_session() -> None:
    """Clear the current session (reset to default)."""
    global _current_user_id
    _current_user_id = None

def is_using_default_user() -> bool:
    """Check if we're using the default hardcoded user ID."""
    return _current_user_id is None 