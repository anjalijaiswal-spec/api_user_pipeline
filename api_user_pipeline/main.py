
import requests
import json
import csv
from datetime import datetime

print(datetime.now())

API_URL = "https://jsonplaceholder.typicode.com/users"

# -----------------------------
# FETCH USERS FROM API
# -----------------------------
def fetch_users():

    try:

        response = requests.get(API_URL)

        if response.status_code == 200:
            print("✓ API request successful")
            return response.json()

        else:
            print(f"✗ API failed: {response.status_code}")
            return []

    except requests.exceptions.RequestException as error:
        print(f"✗ Request error: {error}")
        return []


# -----------------------------
# VALIDATE USERS
# -----------------------------
def validate_user(user):

    if not user.get("name"):
        return False, "Missing name"

    if not user.get("email"):
        return False, "Missing email"

    if "@" not in user.get("email", ""):
        return False, "Invalid email"

    if len(user.get('phone')) < 5:
        return False, "Invalid phone number"
    return True, "Valid user"


# -----------------------------
# PROCESS USERS
# -----------------------------
def process_users(users):

    valid_users = []
    invalid_users = []

    for user in users:

        is_valid, message = validate_user(user)

        print(f"\nChecking: {user['name']}")
        print(f"Result: {message}")

        if is_valid:
            valid_users.append(user)

        else:
            invalid_users.append({
                "user": user,
                "error": message
            })

    return valid_users, invalid_users


# -----------------------------
# SAVE JSON FILE
# -----------------------------
def save_json(filename, data):

    try:

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        print(f"✓ Saved {filename}")

    except Exception as error:
        print(f"✗ Failed saving {filename}: {error}")

# -----------------------------
# SAVE CSV FILE
# -----------------------------

def saved_csv(filename, data):

    try:
        if not data:
            print(f"✗ No data to save to {filename}")
            return

        with open(filename, "w", newline='') as file:
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"✓ Saved {filename}")

    except Exception as error:
        print(f"✗ Failed saving {filename}: {error}")

# -----------------------------
# GENERATE REPORT
# -----------------------------
def generate_report(valid_users, invalid_users):

    print("\n========== REPORT ==========")
    print(f"Valid Users: {len(valid_users)}")
    print(f"Invalid Users: {len(invalid_users)}")
    print("============================")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():

    print("Starting User Data Pipeline...\n")

    users = fetch_users()

    if not users:
        print("No users found")
        return

    valid_users, invalid_users = process_users(users)

    save_json("valid_users.json", valid_users)
    save_json("invalid_users.json", invalid_users)

    saved_csv("valid_users.csv", valid_users)
    save_valid_users_to_text("valid_users.txt", valid_users)

    generate_report(valid_users, invalid_users)

    print("\nPipeline Complete!")

# -----------------------------
# SAVE TEXT FILE
# -----------------------------
def save_valid_users_to_text(filename, users):

    try:
        with open(filename, "w") as file:
            if not users:
                file.write("No valid users found.\n")
                return

            file.write("=" * 50 + "\n")
            file.write("VALID USERS\n")
            file.write("=" * 50 + "\n\n")

            for idx, user in enumerate(users, 1):
                file.write(f"User #{idx}\n")
                file.write(f"  Name: {user.get('name', 'N/A')}\n")
                file.write(f"  Email: {user.get('email', 'N/A')}\n")
                file.write(f"  Phone: {user.get('phone', 'N/A')}\n")
                file.write(f"  Company: {user.get('company', {}).get('name', 'N/A')}\n")
                file.write("-" * 50 + "\n\n")

        print(f"✓ Saved {filename}")

    except Exception as error:
        print(f"✗ Failed saving {filename}: {error}")


# Run program
if __name__ == "__main__":
    main()


