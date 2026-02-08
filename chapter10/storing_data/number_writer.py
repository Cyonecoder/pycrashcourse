import json


numbers = [2, 3, 4, 7, 11, 13]


filename = "numbers.json"

with open(file=filename, mode="w", encoding="utf-8") as f:
    json.dump(numbers, f)
