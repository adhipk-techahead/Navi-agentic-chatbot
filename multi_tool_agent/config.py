import os
from google.adk.models.lite_llm import LiteLlm
# Model configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash-lite")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "")
if OPENAI_BASE_URL:
    # use litellm only if OPENAI_BASE_URL is set otherwise assume it's a Google model.
    MODEL = LiteLlm(model=MODEL_NAME)
else:   
    MODEL = MODEL_NAME
# Other configuration variables can be added here
DEBUG = os.getenv("DEBUG", "false").lower() == "true" 