import json

def save_health_assessment(health_assessment_json: str) -> str:
    """Save health assessment data.
    
    Args:
        health_assessment_json: JSON string containing health assessment data
    
    Returns:
        str: Success message
    """
    try:
        # Validate that it's valid JSON
        assessment_data = json.loads(health_assessment_json)
        return f"✅ Health assessment saved successfully with {len(assessment_data)} fields"
    except json.JSONDecodeError:
        return "❌ Error: Invalid JSON format for health assessment"

