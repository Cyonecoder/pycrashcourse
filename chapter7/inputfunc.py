# message = input("tell me something , and iw ill repeat it back to you :")
# print(message)
# name = input("please enter your name: ")
# print(f"\n hello {name}")

# prompt = "if you tell us who you afre ,m we can personalize the message you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}")
# age = input("how old are you? ")
# age = int(age)
# print(age >= 18)

# rental_car = input("What kind of car do you want to rent? ")

# print(f"\n let me find you a {rental_car}")

# seating = input("How many people are in the dinner group")

# seating_number = int(seating)
# if seating_number > 8:
#     print("You have to wait for a table.")
# else:
#     print("table is ready")
# number_enter = input("enter a number")

# number_entred_int = int(number_enter)
# if number_entred_int % 10 == 0:
#     print(f"{number_enter} is a multiple of 10")
# else:
#     print(f"{number_enter} is a not a multiple of 10 ")
# enter = ""
# while enter != "quit":
#     msg = input("enter a topping: ")
#     enter = msg
#     if msg != "quit":

#         print(f"\n you enter topping {msg} to your pizza")

# age = ""
# while age != "quit":
#     age = input("enter your Age :")
#     if age == "quit":
#         break
#     int_age = int(age)

#     if int_age < 3:
#         print("Ticket price is free")
#     elif int_age >= 3 and int_age <= 12:
#         print("Ticket price is 10$")

#     else:
#         print("Ticket price is 15$")
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]

while "cat" in pets:
    pets.remove("cat")

print(pets)
