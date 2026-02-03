def decide_action(user_request: str) -> dict:
    """
    Decide what tool to use based on user request.
    Returns a structured action plan.
    """

    user_request = user_request.lower()

    if "clean" in user_request or "csv" in user_request:
        return {
            "action": "clean_data",
            "description": "Clean a CSV file"
        }

    return {
        "action": "unknown",
        "description": "No suitable action found"
    }
