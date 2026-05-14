import json

# Multiple users (VERY common in real projects)
users = [
    {
        "name": "Alex",
        "email": "alex@example.com",
        "age": 28
    },
    {
        "name": "Sarah",
        "email": "",
        "age": 31
    },
    {
        "name": "Mike",
        "email": "mike@example.com",
        "age": 16
    },
    {
    "name": "aa",
    "email": "test_est.com",
    "age": 25
    }
]

# Store valid users here
valid_users = []

# Validation function
def validate_user(user):

    if not user.get("name"):
        return False, "Missing name"

    if not user.get("email"):
        return False, "Missing email"
    else:
        if "@" not in user.get("email", ""):
            return False, "Invalid mail"

    if user.get("age", 0) < 21:
        return False, "Underage"

    return True, "Valid user"

# Process all users
for user in users:

    is_valid, message = validate_user(user)

    print(f"\nChecking: {user['name']}")
    print(f"Result: {message}")

    if is_valid:
        valid_users.append(user)

# Save valid users to file

try:
    with open(".venv/lib/python3.13/valid_users.json", "w") as file:
        json.dump(valid_users, file, indent=2)
    print("\nSaved valid users successfully")

except exception as error:
    print(f"Something went wrong: {error}")
    for user in users:
