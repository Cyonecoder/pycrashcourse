file_path = "text_files/pi_digits.txt"
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(repr(contents))
#     print(repr(contents.rstrip()))
# print(contents)


# with open(file_path) as file_object:
#     """read file by file"""
#     for line in file_object:
#         print(line.rstrip())

with open(file_path) as file_object:
    """read file by file"""
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
