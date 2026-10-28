def validate_user(username: str):
    if not username or not username.strip():
        raise ValueError("Username cannot be empty")
    return {"username": username, "status": "active"}