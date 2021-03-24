import datetime
from dotenv import load_dotenv
import requests
import os

load_dotenv()
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

headers = {
    "X-USER-TOKEN": TOKEN
}

# Step 1. Create a user
"""
user_params = {
    "token": TOKEN,
    "username": "curlos",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)

print(response.text)"""

# Step 2. Create a graph

"""graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)"""

# Step 3. Post a pixel to graph
"""pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

pixel_config = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "4327232445"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)"""

# Step 4. Update an existing pixel using a put request

"""today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{yesterday.strftime('%Y%m%d')}"

pixel_config = {
    "quantity": "70"
}
response = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)"""

# Step 5. Delete an existing pixel
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{yesterday.strftime('%Y%m%d')}"

response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)