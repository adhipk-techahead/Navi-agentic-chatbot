def update_hippa_consent(newvalue: str) -> str:
    """Update HIPAA consent status.
    
    Args:
        newvalue: Whether HIPAA consent is accepted ("true" or "false")
    
    Returns:
        str: Success message
    """
    # Note: In ADK LlmAgent context, state updates happen automatically
    # through the agent's output_key mechanism
    if newvalue.lower() not in ['true', 'false']:
        return f"❌ Error: HIPAA consent must be 'true' or 'false', got: {newvalue}"
    
    return f"✅ HIPAA consent updated to: {newvalue}"
   
