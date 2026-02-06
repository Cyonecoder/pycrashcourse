filename = "guest.txt"

with open(file=filename, mode="w") as file_object:

    name = input("Enter the guest name:")
    file_object.write(f"{name}\n")
