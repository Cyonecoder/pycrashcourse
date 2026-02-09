import json


filename = "favorite_numbers.json"


favorite_num = input("Enter your favorite number: ")


with open(file=filename, mode="w") as f:
    json.dump(favorite_num, f)
    print(f"your favorite number {favorite_num} is storred ")
