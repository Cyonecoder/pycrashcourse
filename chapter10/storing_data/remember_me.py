import json


# username = input("Whats your name? ")
# filename = "username.json"
# with open(file=filename, mode="w") as f:
#     json.dump(username, f)
#     print(f"We will remember you when you comeback,{username}! ")


def greet_user():
    filename = "username.json"
    try:
        with open(file=filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(file=filename, mode="w") as f:
            json.dump(username, f)
            print(f"We will remember you when you comeback,{username}! ")
    else:
        print(f"Welcome back, {username}!")


greet_user()
