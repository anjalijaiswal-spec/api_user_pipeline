import json

dict = {"a":5,"b":10}
print(dict["a"])

user_data = {
    "name": "Alex",
    "email": "alex@example.com",
    "age": 28,
    "skills": ["Python", "APIs", "Automation"],
    "is_active": True
}

user_data['name'] = "Anjali"
user_data['age'] = 16
user_data['skills'].append("git")
user_data['country']='India'
user_data['user_type']='freelancer'
print(f"User: {user_data['name']}")
print(f"Email: {user_data['email']}")
print(f"Country: {user_data['country']}")
print(f"user_type: {user_data['user_type']}")

print("\nSkills:")
for skill in user_data['skills']:
    print(f"- {skill}")

if user_data['age'] >= 18:
    print("Eligible for freelance work")
else:
    print("Not eligible")

def validate_user(user):
    if not user.get('email'):
        return False

    if not user.get('name'):
        return False

    return True

print("\nValidation:", validate_user(user_data))

with open('.venv/lib/python3.13/user_data.json', 'w') as file:
    json.dump(user_data, file, indent=2)

print("\nSaved JSON file successfully")
