from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nPlease give a first name: ")
    if first == "q":
        break
    last = input("Please give a last name: ")
    if last == "q":
        break
    formmatted_name = get_formatted_name(first, last)
    print(f"\t neatly formatted name: {formmatted_name}. ")
