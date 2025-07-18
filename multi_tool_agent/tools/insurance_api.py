def get_insurance_record(user_id: str) -> dict:
    """Mock: Fetches insurance record for a user."""
    return {
        "policy_number": "MOCK123456",
        "coverage": "Comprehensive Health",
        "copay": "$20",
        "deductible": "$500",
        "max_out_of_pocket": "$2000",
        "covered_services": ["Primary Care", "Specialist", "Emergency"],
        "exclusions": ["Cosmetic Surgery"],
    } 