from pizza import make_pizza

# def greet_user():
#     """Display a simple greeting"""
#     print("Hello!")


# def greet_user2(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}")


# greet_user()
# greet_user2("jessie")


# def display_message():
#     print("im learning this function")


# def favorite_book(title):
#     print(f"my favorite book is {title}")


# display_message()

# favorite_book("Miracle morning")


# def describe_pet(animal_type="no type", pet_name="no name"):
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# describe_pet("hamster", "harry")
# describe_pet("dog", "willie")
# describe_pet()


# def make_shirt(size="large", message="I Love Python"):
#     print(f"size of the shirt :{size}\nmessage: {message}")


# make_shirt("medium")
# make_shirt("large")
# make_shirt("16/9", "this is live on mtv")


# def get_formatted_name(first_name, last_name, middle_name=""):
#     if middle_name:

#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix", "lee")
# print(musician)
# musician = get_formatted_name("jimi", "hendrix")
# print(musician)


# def build_person(first_name, last_name, age=None):
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person["age"] = age
#     return person


# musician = build_person("jimi", "hendrix", 55)
# print(musician)


# def get_formatted_name(first_name, last_name, middle_name=""):
#     if middle_name:

#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()


# while True:
#     print("\n Please tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Last name: ")

#     if f_name == "q":
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


def city_country(city, country):
    formatted_city_name = f"{city}, {country}"
    return formatted_city_name


# city_countryname = city_country("Casblanca", "Morocco")
# print(city_countryname)
# city_countryname = city_country("Bangkok", "Thailand")
# print(city_countryname)
# city_countryname = city_country("New York", "USA")
# print(city_countryname)


# def make_album(artist_name, album_title, songsNb=None):
#     album_artist = {"artist": artist_name, "album": album_title}
#     if songsNb:
#         album_artist["songsNb"] = songsNb
#     return album_artist


# album_artist = make_album("toto", "mghayar")
# print(album_artist)
# album_artist = make_album("toto", "camelon", 9)
# print(album_artist)

# while True:
#     name = input("enter name: ")
#     if name == "q":
#         break
#     album = input("enter album: ")
#     if album == "q":
#         break
#     album_artist = make_album(name, album)
#     print(album_artist)


# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)


# usernames = ["hannah", "ty", "margot"]
# greet_users(usernames)

# unprinted_designs = ["phone cases", "robot pendant", "dodecahedron"]
# completed_models = []
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing mnodel: {current_design}")
#     completed_models.append(current_design)


# print("\n the following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing mnodel: {current_design}")
#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     print("\nThe following models have been printed")
#     for completed_model in completed_models:
#         print(completed_model)


# unprinted_designs = ["phone cases", "robot pendant", "dodecahedron"]
# completed_models = []
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)


# def make_pizza(*toppings):
#     print(toppings)


# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza("peperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")


# def make_pizza(size, *toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza(16, "peperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# def build_profile(first, last, **user_info):
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# user_profile = build_profile(
#     "albert", "einstein", location="princeton", field="physics"
# )
# print(user_profile)
# pizza.make_pizza(16, "peperoni")
# pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")
# make_pizza(16, "peperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")

messages = ["text1", "text2", "text3"]
sent_messages = []


def show_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)
    print(f"message is{messages},\nsent_messages is {sent_messages}")


show_messages(messages[:], sent_messages)


def make_sandwich(*sandwich_add_ons):
    for item in sandwich_add_ons:
        print(item)


make_sandwich("hq", "sd", "sdde")


def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


me = build_profile("simo", "khass", tall=180, weight=70, city="Sale")
print(me)


def build_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info


car = build_car("BMW", "M4", style="coupe", year=2026, price=67_000)
print(car)
