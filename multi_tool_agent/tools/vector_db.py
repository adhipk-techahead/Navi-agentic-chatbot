def query_vector_db(video_id: str, user_preferences: dict) -> dict:
    """Mock: Queries vectorDB for validated medical claims and citations for a video/article."""
    # Mock response with validated claims and citations
    return {
        "video_id": video_id,
        "claims": [
            {
                "id": "claim_001",
                "text": "Regular exercise reduces cardiovascular disease risk by 30%",
                "citation": "American Heart Association, 2023",
                "confidence": 0.95
            },
            {
                "id": "claim_002", 
                "text": "Mediterranean diet improves heart health and longevity",
                "citation": "Journal of Cardiology, 2022",
                "confidence": 0.92
            },
            {
                "id": "claim_003",
                "text": "Stress management techniques lower blood pressure",
                "citation": "WHO Guidelines, 2023",
                "confidence": 0.88
            }
        ],
        "user_relevance_score": 0.87,
        "total_claims": 3
    }

def get_user_medical_preferences(user_id: str) -> dict:
    """Mock: Retrieves user's medical preferences and profile for content relevance."""
    return {
        "user_id": user_id,
        "interests": ["cardiovascular health", "nutrition", "stress management"],
        "medical_conditions": ["hypertension", "diabetes"],
        "preferred_content_type": "video",
        "expertise_level": "intermediate"
    } 