filename = "programing.txt"
"""write into a file"""
with open(file=filename, mode="w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
""" append into a file """
with open(file=filename, mode="a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write(
        "I love creating apps that can run in browsers and new browsers games.\n"
    )
