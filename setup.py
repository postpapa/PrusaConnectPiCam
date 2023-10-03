import requests
import json
import os
import uuid

fingerprint = str(uuid.uuid4())
token = input("Enter the Token for the 'Other camera': ")
new_name = input("Enter a new name for the 'Other camera' for easier recognition: ")

# Define the request headers
headers = {
    "Content-Type": "application/json",
    "Token": token,
    "Fingerprint": fingerprint,
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

# Define the request URL
url = "https://connect.prusa3d.com/c/info"

# Construct the request payload
payload = {
    "config": {
        "camera_id": fingerprint,
        "path": "/dev/video0",
        "name": new_name,
        "driver": "V4L2",
        "trigger_scheme": "TEN_SEC",
        "resolution": {
            "width": 1280,
            "height": 720
        }
    },
    "options": {
        "available_resolutions": [
            {
                "width": 1280,
                "height": 720
            }
        ]
    },
    "capabilities": ["trigger_scheme"]
}

response = requests.put(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Request was successful.")
    try:
        filename = "sendscreenshot.py"

        with open(filename, 'r') as file:
            content = file.read()

        content = content.replace("CAMERATOKEN", token)
        content = content.replace("CAMERAFINGERPRINT", fingerprint)

        with open(filename, 'w') as file:
            file.write(content)

    except FileNotFoundError:
        print('The file "{filename}" was not found.')

else:
    print("Request failed with status code: {response.status_code}")
    print("Response content:")
    print(response.text)
