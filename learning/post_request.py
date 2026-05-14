import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

# Data to send
new_post = [{
    "title": "My Automation Journey",
    "body": "This is my first POST request",
    "userId": 15,
    "category": "Programming",
    "Id":101
    },
    {
        "title": "My Automation Journey",
        "body": "This is my second POST request",
        "userId": 10,
        "category": "Programming",
        "Id":102
    },
    {
        "title": "My Automation Journey",
        "body": "This is my third POST request",
        "userId": 11,
        "category": "Programming",
        "Id":103
    }
    ,]

try:

    # Send POST request
    data = []
    for posts in new_post:
        response = requests.post(url, json=posts)

        # Check status
        if response.status_code == 201:

            print("POST request successful!\n")

            # Convert response JSON
            response_data = response.json()

            print("Created Post:")
            print(f"ID: {response_data['id']}")
            print(f"Title: {response_data['title']}")
            print(f"Body: {response_data['body']}")


            data.append(response_data)



        else:
            print(f"Failed with status code: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")

print (f"\n {data}")


with open("created_post.json", "r") as file:
        data1=json.load(file)
print(data1)

with open("created_post.json", "w") as file:
        json.dump(data, file, indent=2)

import os
print (os.getcwd())