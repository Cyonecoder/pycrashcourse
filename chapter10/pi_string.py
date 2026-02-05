file_name = "pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()


pi_string = ""
for line in lines:
    pi_string += line.strip()
birthday = input("ENTER YOUR BIRTHDAY: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# print(pi_string[:52])
# print(len(pi_string))
