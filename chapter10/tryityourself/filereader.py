filesnames = ["cats.txt", "dogs.txt"]

for file in filesnames:
    try:
        with open(file=file, mode="r") as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"file not found")
    else:
        print(contents)
