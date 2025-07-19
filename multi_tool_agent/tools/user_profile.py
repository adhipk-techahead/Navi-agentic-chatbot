# In-memory user profile storage (replace with database in production)
from typing import Optional
from multi_tool_agent.tools.session_management import get_current_user_id

# JSON Schema for user profile validation and type information
USER_PROFILE_SCHEMA = {
        "user_id": "",
        "name": "",
        "age": "",
        "gender": "",
        "demographics": "",
        "height": "",
        "weight": "",
        "bmi": "",
        "bmi_category": "",
        "occupation": "",
        "lifestyle_score": "",
        "exercise_frequency": "",
        "smoking": "",
        "drinking": "",
        "diet": "",
        "allergies": "",
        "stress_level": "",
        "family_history": "",
        "pre_existing_conditions": "",
        "current_medications": "",
        "hipaa_accepted": "",
        "profile_completed": "",
        "created_at": "",
        "updated_at": ""
    }

mock_user_profile = {
        "user_id": "user_123",
        "name": "David",
        "age": "42",
        "gender": "male",
        "demographics": "Caucasian",
        "height": "6'4",
        "weight": "150 lb",
        "bmi": "12",
        "bmi_category": "fit",
        "occupation": "Software Engineer",
        "exercise": "running, bouldering",
        "exercise_frequency": "weekly",
        "smoking": "no",
        "drinking": "occasional",
        "diet": "protien rich, low carb",
        "allergies": "bees",
        "stress_level": "high",
        "family_history": "mother has diabetes",
        "pre_existing_conditions": "none",
        "current_medications": "sleep medication: ambien 20mg daily for 10 years, pain medication: tylenol 500mg weekly",
        "hipaa_accepted": "true",
        "profile_completed": "true",
        "created_at": "2025-01-01",
        "updated_at": "2025-01-01"
}




def get_user_profile(user_id: Optional[str] = None) -> dict:
    """Get complete user profile including onboarding data. Uses current session user ID if none provided."""
    
    return mock_user_profile

def update_user_profile(field: str, value: str, user_id: Optional[str] = None) -> bool:
   mock_user_profile[field] = value
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
