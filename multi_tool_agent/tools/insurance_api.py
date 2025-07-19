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

def get_healthcare_providers(user_id: str) -> list:
    """Mock: Fetches healthcare providers for a user."""
    return [
        {
            "name": "Dr. John Doe",
            "specialty": "Cardiologist",
            "address": "123 Main St, Anytown, USA",
            "phone": "555-1234",
        },
        {
            "name": "Dr. Jane Smith",
            "specialty": "Primary Care",
            "address": "456 Elm St, Anytown, USA",
            "phone": "555-5678",
        },
        {
            "name": "Dr. Jim Beam",
            "specialty": "Dentist",
            "address": "789 Oak St, Anytown, USA",
            "phone": "555-9101",
        },
        {
            "name": "Dr. Jill Johnson",
            "specialty": "Therapist",
            "address": "101 Pine St, Anytown, USA",
            "phone": "555-1212",
        },
        
    ]