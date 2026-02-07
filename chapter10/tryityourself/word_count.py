filename = "../analyzingText/alice.txt"

try:
    with open(file=filename, mode="r", encoding="utf-8") as f:

        content = f.read()
        word_count = content.count("yes")

except FileNotFoundError:
    print(f"file not found")

else:
    print(f"find {word_count} yes")
