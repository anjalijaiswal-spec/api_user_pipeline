import requests

# API endpoint
# url =  "https://swapi.tech/api/people/1"
url = "https://jsonplaceholder.typicode.com/users"
# Send GET request

try:
    response = requests.get(url)

    # Check if request worked
    if response.status_code == 200:

        print("Request successful!")

        # Convert JSON response into Python data
        users = response.json()

        print(f"\nTotal users: {len(users)}")
        # for user in users:
        #         print("\n-------------------")
        #         print(f"Name: {user['name']}")
        #         print(f"Email: {user['email']}")
        #         print(f"City: {user['address']['city']}")
        #         print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

import json

with open(".venv/lib/python3.13/users_multi.json", "w") as file:
    json.dump(users, file, indent=2)

for user in users:
    print(f"\n name:{user['name']}")
    print(f" user_names:{user['username']}")
    print(f" phone:{user['phone']}")

#Count city-wise users
city_count = {}
for user in users:
    city = user['address']['city']
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print(city_count.keys())
print(city_count)
for city in city_count.keys():
    print(f"City: {city}, count: {city_count[city]}")