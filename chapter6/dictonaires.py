person = {
    "first_name": "simo",
    "last_name": "khas",
    "age": 33,
    "city": "california",
    "favorite_number": [3, 33, 333],
}
person2 = {
    "first_name": "amo",
    "last_name": "szds",
    "age": 23,
    "city": "NYC",
    "favorite_number": [4, 44, 444],
}
person3 = {
    "first_name": "salima",
    "last_name": "fdf",
    "age": 43,
    "city": "Paris",
    "favorite_number": [7, 77, 777],
}
people = [person, person2, person3]
# person['sa']=1
# person['bo']=2
# person['ka']=3
# person['ni']=4
# person['do']=5
# person['list']='[]'
# person['tuple']='(t1,t2)'
# person['string']='str'
# person['if statement ']= 'if else elif'
# person['bool']='true or false'
# for k,v in person.items():
#     print(k,':',v)

# for i in person:
#     print(i)

for person in people:
    for k, v in person.items():
        print(k, ":", v)
    print("*//*//" * 5)

pet1 = {"kind": "dog", "owner": "samir"}
pet2 = {"kind": "cat", "owner": "faisal"}
pet3 = {"kind": "dog", "owner": "kasim"}
pets = [pet1, pet2, pet3]

for pet in pets:
    for k, v in pet.items():
        print(k, ":", v)
    print("*//*//" * 5)
favorite_places = {"samir": "antalya", "faisal": "phuket", "kasim": "barcelona"}
for k, v in favorite_places.items():
    print(k, ":", v)

for person in people:

    print(
        person["first_name"],
        person["last_name"],
        "favorite_number",
        ":",
        person["favorite_number"],
    )
    print("*//*//" * 5)

cities = {
    "rabat": {
        "country": "Morocco",
        "population": 2_000_000,
        "fact": "older than 9200 years",
    },
    "Paris": {
        "country": "France",
        "population": 31_000_000,
        "fact": "arts are good their",
    },
    "Bogota": {
        "country": "Colombia",
        "population": 30_000_000,
        "fact": "latina best place",
        "oled": {"oled1": "ooooooo"},
    },
}

for city, info in cities.items():

    print(city, ":", info["country"], info["population"], info["fact"])
    if "oled" in info:
        for k, v in info.items():
            print("  ", k, ":", v)

    print("*//*//" * 5)
