import json

filename = "username.json"

with open(file=filename) as f:

    username = json.load(f)
    print(f"Welcome back, {username}")
