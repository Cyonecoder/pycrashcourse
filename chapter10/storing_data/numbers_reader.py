import json

filename = "numbers.json"
with open(file=filename) as f:
    numbers = json.load(f)

print(numbers)
