import json


filename = "favorite_numbers.json"
try:
    with open(file=filename) as f:
        fav_num = json.load(f)
        print(f" “I know your favorite number! It’s {fav_num}.”")


except FileNotFoundError:

    print(f"file {filename}not found")
