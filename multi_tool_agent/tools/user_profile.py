# In-memory user profile storage (replace with database in production)
from typing import Any, Dict, List, Optional
import json
from multi_tool_agent.tools.session_management import get_current_user_id

user_profiles = {}

# JSON Schema for user profile validation and type information
USER_PROFILE_SCHEMA = {
    "type": "object",
    "properties": {
        "user_id": {"type": "string"},
        "name": {"type": "string", "minLength": 1},
        "age": {"type": "integer", "minimum": 0, "maximum": 120},
        "gender": {"type": "string", "enum": ["male", "female", "other", "prefer_not_to_say"]},
        "demographics": {"type": "object"},
        "height": {"type": "number", "minimum": 50, "maximum": 250, "description": "Height in centimeters"},
        "weight": {"type": "number", "minimum": 20, "maximum": 300, "description": "Weight in kilograms"},
        "bmi": {"type": "number", "minimum": 10, "maximum": 60},
        "bmi_category": {"type": "string", "enum": ["Underweight", "Normal weight", "Overweight", "Obese", "Unknown"]},
        "occupation": {"type": "string"},
        "lifestyle_score": {"type": "integer", "minimum": 1, "maximum": 5, "description": "1=Very sedentary, 5=Very active"},
        "exercise_frequency": {"type": "string", "enum": ["never", "rarely", "sometimes", "often", "daily"]},
        "smoking": {"type": "string", "enum": ["never", "former", "current", "occasional"]},
        "drinking": {"type": "string", "enum": ["never", "rarely", "moderate", "heavy"]},
        "diet": {"type": "string", "enum": ["omnivore", "vegetarian", "vegan", "pescatarian", "keto", "paleo", "other"]},
        "allergies": {"type": "array", "items": {"type": "string"}},
        "stress_level": {"type": "integer", "minimum": 1, "maximum": 10, "description": "1=Very low stress, 10=Very high stress"},
        "family_history": {"type": "array", "items": {"type": "string"}},
        "pre_existing_conditions": {"type": "array", "items": {"type": "string"}},
        "current_medications": {"type": "array", "items": {"type": "string"}},
        "hipaa_accepted": {"type": "boolean"},
        "profile_completed": {"type": "boolean"},
        "created_at": {"type": "string"},
        "updated_at": {"type": "string"}
    },
    "required": ["user_id"]
}

def get_profile_schema() -> str:
    """Get the JSON schema for user profile as a formatted string."""
    return json.dumps(USER_PROFILE_SCHEMA, indent=2)

def get_user_profile(user_id: Optional[str] = None) -> dict:
    """Get complete user profile including onboarding data. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    return user_profiles.get(user_id, {
        "user_id": user_id,
        "name": None,
        "age": None,
        "gender": None,
        "demographics": {},
        "height": None,
        "weight": None,
        "bmi": None,
        "bmi_category": None,
        "occupation": None,
        "lifestyle_score": None,
        "exercise_frequency": None,
        "smoking": None,
        "drinking": None,
        "diet": None,
        "allergies": [],
        "stress_level": None,
        "family_history": [],
        "pre_existing_conditions": [],
        "current_medications": [],
        "hipaa_accepted": False,
        "profile_completed": False,
        "created_at": None,
        "updated_at": None
    })

def update_user_profile(field: str, value: str, user_id: Optional[str] = None) -> bool:
    """Update a specific field in user profile. Value should be a string that will be parsed according to the schema. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    if user_id not in user_profiles:
        user_profiles[user_id] = get_user_profile(user_id)
    
    user_profiles[user_id][field] = value
    user_profiles[user_id]["updated_at"] = "now"
    return True

def update_multiple_profile_fields(updates: Dict[str, Any], user_id: Optional[str] = None) -> bool:
    """Update multiple fields in user profile at once. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    if user_id not in user_profiles:
        user_profiles[user_id] = get_user_profile(user_id)
    
    for field, value in updates.items():
        user_profiles[user_id][field] = value
    
    user_profiles[user_id]["updated_at"] = "now"
    return True

def calculate_bmi(height_cm: float, weight_kg: float) -> Optional[float]:
    """Calculate BMI from height (cm) and weight (kg)."""
    if height_cm <= 0 or weight_kg <= 0:
        return None
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)

def get_bmi_category(bmi: Optional[float]) -> str:
    """Get BMI category based on calculated BMI."""
    if bmi is None:
        return "Unknown"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def generate_welcome_message(user_id: Optional[str] = None) -> str:
    """Generate personalized welcome message based on user profile. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    profile = get_user_profile(user_id)
    
    if not profile["name"]:
        return "Hi! I'm Navi, your health assistant. I'm here to help you set up your health profile. Should we begin?"
    
    # Personalized welcome based on available data
    welcome_parts = [f"Hi {profile['name']}! I'm Navi, your health assistant."]
    
    if profile["age"]:
        welcome_parts.append(f"I see you're {profile['age']} years old.")
    
    if profile["bmi"] and profile["bmi_category"]:
        welcome_parts.append(f"Your BMI is {profile['bmi']} ({profile['bmi_category']}).")
    
    if profile["pre_existing_conditions"]:
        conditions = ", ".join(profile["pre_existing_conditions"][:2])  # Show first 2
        welcome_parts.append(f"I notice you have {conditions} in your medical history.")
    
    if profile["current_medications"]:
        meds = ", ".join(profile["current_medications"][:2])  # Show first 2
        welcome_parts.append(f"You're currently taking {meds}.")
    
    welcome_parts.append("How can I help you today?")
    
    return " ".join(welcome_parts)

def get_profile_completion_percentage(user_id: Optional[str] = None) -> int:
    """Calculate profile completion percentage. Uses current session user ID if none provided."""
    if user_id is None:
        user_id = get_current_user_id()
    
    profile = get_user_profile(user_id)
    required_fields = [
        "name", "age", "gender", "height", "weight", "occupation",
        "lifestyle_score", "exercise_frequency", "smoking", "drinking",
        "diet", "allergies", "stress_level", "family_history",
        "pre_existing_conditions", "current_medications"
    ]
    
    completed_fields = sum(1 for field in required_fields if profile.get(field) is not None)
    return round((completed_fields / len(required_fields)) * 100)

def get_all_user_profiles() -> dict:
    """Get all user profiles (for debugging/admin purposes)."""
    return user_profiles 