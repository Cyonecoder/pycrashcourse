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


def make_album(artist_name, album_title, songsNb=None):
    album_artist = {"artist": artist_name, "album": album_title}
    if songsNb:
        album_artist["songsNb"] = songsNb
    return album_artist


album_artist = make_album("toto", "mghayar")
print(album_artist)
album_artist = make_album("toto", "camelon", 9)
print(album_artist)
