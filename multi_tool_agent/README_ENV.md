# Environment Configuration

This project uses environment variables for configuration. Here's how to set them up:

## Required Environment Variables

### MODEL
The Google AI model to use for all agents.

**Default**: `gemini-2.0-flash-lite`

**Options**:
- `gemini-2.0-flash-lite` (recommended for speed)
- `gemini-2.0-flash` (standard)
- `gemini-2.0-exp` (experimental)
- `gemini-1.5-flash` (alternative)

**Example**:
```bash
export MODEL=gemini-2.0-flash-lite
```

### OPENAI_BASE_URL (Optional)
If set, uses LiteLLM for model access. If not set, assumes Google model.

**Example**:
```bash
export OPENAI_BASE_URL=https://api.openai.com/v1
```

## Session Management

### Setting User ID from Session

The system uses a session-based user ID that can be set dynamically. By default, it uses `"user_123"`.

#### Option 1: Environment Variable
```bash
export NAVI_USER_ID=your_actual_user_id
```

#### Option 2: Programmatically
```python
from multi_tool_agent.tools.session_management import set_current_user_id

# Set user ID from your authentication system
set_current_user_id("user_456")
```

#### Option 3: Web Framework Integration
```python
# Flask example
from multi_tool_agent.session_integration import initialize_session_from_request

@app.before_request
def setup_session():
    initialize_session_from_request(request)

# FastAPI example
from multi_tool_agent.session_integration import initialize_session_from_request

@app.post("/chat")
async def chat(request: Request):
    initialize_session_from_request(request)
    # User ID is now available to all agents
```

#### Option 4: Check Session Status
```python
from multi_tool_agent.session_integration import check_session_status

status = check_session_status()
print(f"Current user: {status['user_id']}")
print(f"Using default: {status['using_default']}")
```

## Optional Environment Variables

### DEBUG
Enable debug mode for additional logging.

**Default**: `false`

**Example**:
```bash
export DEBUG=true
```

## Setting Up Environment Variables

### Option 1: Export in Shell
```bash
export MODEL=gemini-2.0-flash-lite
export NAVI_USER_ID=user_456
export DEBUG=false
```

### Option 2: Create .env File
Create a `.env` file in the project root:
```bash
MODEL=gemini-2.0-flash-lite
NAVI_USER_ID=user_456
DEBUG=false
```

Then load it in your application:
```python
from dotenv import load_dotenv
load_dotenv()
```

### Option 3: System Environment
Set in your system environment variables permanently.

## Deployment (Render.com)

In your Render dashboard, add environment variables:

1. Go to your service settings
2. Navigate to "Environment" tab
3. Add environment variables:
   - `MODEL`: `gemini-2.0-flash-lite`
   - `NAVI_USER_ID`: `your_user_id` (or set programmatically)
   - `DEBUG`: `false`

## Verification

You can verify the configuration is working by checking the config:

```python
from multi_tool_agent.config import MODEL, DEBUG
from multi_tool_agent.session_integration import check_session_status

print(f"Model: {MODEL}")
print(f"Debug: {DEBUG}")
print(f"Session: {check_session_status()}")
```

## Session Integration Examples

See `multi_tool_agent/session_integration.py` for complete examples of how to integrate session management with:

- Flask applications
- FastAPI applications  
- Authentication systems
- Environment variables 