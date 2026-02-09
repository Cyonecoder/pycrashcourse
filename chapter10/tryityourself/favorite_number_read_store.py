import json


filename = "favorite_numbers.json"


try:
    with open(file=filename) as f:
        fav_num = json.load(f)
        if fav_num:
            print(f"I know your favorite number! It’s {fav_num}.")

except FileNotFoundError:

    with open(file=filename, mode="w") as f:

        favorite_num = input("Enter your favorite number: ")
        json.dump(favorite_num, f)
        print(f"your favorite number {favorite_num} is storred ")
