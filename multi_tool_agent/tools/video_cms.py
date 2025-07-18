def get_video_metadata(video_id: str) -> dict:
    return {
        "title": "Understanding Hypertension",
        "duration": "5:32",
        "id": video_id,
    }

def get_transcript_excerpt(video_id: str, timestamp: str = "00:45") -> str:
    return "At 00:45, the video explains the importance of regular blood pressure monitoring."

def get_claims_list(video_id: str) -> list:
    return [
        {"id": "claim1", "text": "Hypertension increases risk of heart disease."},
        {"id": "claim2", "text": "Lifestyle changes can help manage blood pressure."},
    ]

def get_citations_list(video_id: str) -> list:
    return [
        {"id": "cite1", "source": "Journal of Cardiology, 2021"},
        {"id": "cite2", "source": "WHO Guidelines, 2020"},
    ] 