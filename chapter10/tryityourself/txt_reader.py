with open("learning_python.txt") as file_object:
    content = file_object.read()
    content = content.replace("python", "C++")
print(content)
with open("learning_python.txt") as file_object:
    for line in file_object:
        line = line.replace("python", "C++")
        print(line)

with open("learning_python.txt") as file_object:
    lines = file_object.readlines()
    lines = [line.replace("python", "C++") for line in lines]
print(lines)
