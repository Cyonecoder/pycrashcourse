import json


username = input("Whats your name? ")
filename = "username.json"
with open(file=filename, mode="w") as f:
    json.dump(username, f)
    print(f"We will remember you when you comeback,{username}! ")
