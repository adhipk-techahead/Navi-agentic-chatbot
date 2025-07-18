# In-memory mock DB
user_onboarding_progress = {}

def get_onboarding_progress(user_id: str) -> str:
    return user_onboarding_progress.get(user_id, "not_started")

def update_onboarding_progress(user_id: str, progress: str) -> bool:
    user_onboarding_progress[user_id] = progress
    return True 