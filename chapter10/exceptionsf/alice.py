filename = "alice.txt"


try:
    with open(file=filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry file {filename} not found ")
