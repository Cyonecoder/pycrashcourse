filename = "alice.txt"


def count_words(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry , the file {filename} dose not exist")
        pass
    else:
        words = contents.split()

        numwords = len(words)
        print(f"The file {filename} has about {numwords} words.")


filenames = [
    "alice.txt",
    "siddhartha.txt",
    "moby_dick.txt",
    "little_women.txt",
    "saddie.txt",
]
for file in filenames:
    count_words(filename=file)
