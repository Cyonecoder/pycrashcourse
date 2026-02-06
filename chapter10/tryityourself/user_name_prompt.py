# filename = "guest.txt"

# with open(file=filename, mode="w") as file_object:

#     name = input("Enter the guest name:")
#     file_object.write(f"{name}\n")

# filenamebook = "guest_book.txt"


# f = True
# while f:
#     with open(file=filenamebook, mode="+a") as file_object:
#         name = input("Enter the guest name:")
#         if name != "q":
#             print(f"Hello, {name}")
#             file_object.write(f"{name}\n")
#         else:
#             f = False
# filenamebook = "guest_book.txt"

fileresponses = "programming_responses.txt"
f = True
while f:
    with open(file=fileresponses, mode="+a") as file_object:
        name = input("For what reason you like programming:")
        if name != "q":

            file_object.write(f"{name}\n")
        else:
            f = False
