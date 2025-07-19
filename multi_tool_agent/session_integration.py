"""
Session Integration Helper

This module shows how to integrate the session management with your application.
You can use this to set the user ID from your authentication system.
"""

from multi_tool_agent.tools.session_management import (
    set_current_user_id, 
    get_current_user_id, 
    get_session_info,
    is_using_default_user,
    clear_session
)

def initialize_session_from_auth(user_id: str) -> None:
    """
    Initialize session with user ID from your authentication system.
    
    Example usage:
        # After user logs in
        user_id = get_user_from_auth_token(token)
        initialize_session_from_auth(user_id)
    """
    set_current_user_id(user_id)
    print(f"Session initialized for user: {user_id}")

def initialize_session_from_request(request) -> None:
    """
    Initialize session from a web request (Flask/FastAPI example).
    
    Example usage:
        # In your Flask/FastAPI route
        user_id = request.headers.get('X-User-ID') or request.cookies.get('user_id')
        if user_id:
            initialize_session_from_request(request)
    """
    # Extract user ID from request (customize based on your setup)
    user_id = None
    
    # Try different sources
    if hasattr(request, 'headers'):
        user_id = request.headers.get('X-User-ID')
    
    if not user_id and hasattr(request, 'cookies'):
        user_id = request.cookies.get('user_id')
    
    if not user_id and hasattr(request, 'args'):
        user_id = request.args.get('user_id')
    
    if not user_id and hasattr(request, 'json'):
        user_id = request.json.get('user_id') if request.json else None
    
    if user_id:
        set_current_user_id(user_id)
        print(f"Session initialized from request for user: {user_id}")
    else:
        print("No user ID found in request, using default user")

def initialize_session_from_environment() -> None:
    """
    Initialize session from environment variable (useful for testing/deployment).
    
    Example usage:
        # Set environment variable
        export NAVI_USER_ID=user_456
        # Then call this function
    """
    import os
    user_id = os.getenv('NAVI_USER_ID')
    if user_id:
        set_current_user_id(user_id)
        print(f"Session initialized from environment for user: {user_id}")
    else:
        print("No NAVI_USER_ID in environment, using default user")

def check_session_status() -> dict:
    """
    Check the current session status.
    
    Returns:
        dict: Session information including user ID and whether using default
    """
    session_info = get_session_info()
    session_info['using_default'] = is_using_default_user()
    return session_info

# Example usage functions
def example_flask_integration():
    """
    Example of how to integrate with Flask.
    
    In your Flask app:
    """
    example_code = '''
    from flask import Flask, request
    from multi_tool_agent.session_integration import initialize_session_from_request
    
    app = Flask(__name__)
    
    @app.before_request
    def setup_session():
        """Set up session before each request."""
        initialize_session_from_request(request)
    
    @app.route('/chat', methods=['POST'])
    def chat():
        # Session is already set up by before_request
        user_message = request.json.get('message')
        # Your chat logic here - user ID is automatically available
        return {"response": "Chat response"}
    '''
    print("Flask Integration Example:")
    print(example_code)

def example_fastapi_integration():
    """
    Example of how to integrate with FastAPI.
    
    In your FastAPI app:
    """
    example_code = '''
    from fastapi import FastAPI, Request, Depends
    from multi_tool_agent.session_integration import initialize_session_from_request
    
    app = FastAPI()
    
    async def setup_session(request: Request):
        """Dependency to set up session."""
        initialize_session_from_request(request)
    
    @app.post("/chat")
    async def chat(request: Request, session=Depends(setup_session)):
        user_message = await request.json()
        # Your chat logic here - user ID is automatically available
        return {"response": "Chat response"}
    '''
    print("FastAPI Integration Example:")
    print(example_code)

if __name__ == "__main__":
    # Example usage
    print("=== Session Integration Examples ===")
    
    # Check initial state
    print("Initial session:", check_session_status())
    
    # Set user ID manually
    initialize_session_from_auth("user_456")
    print("After setting user ID:", check_session_status())
    
    # Clear session
    clear_session()
    print("After clearing session:", check_session_status())
    
    # Show integration examples
    example_flask_integration()
    example_fastapi_integration() 