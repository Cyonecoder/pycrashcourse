def city_function(city, country, population=""):
    """Fuction that return city and name"""
    if population:
        city_country_formatted = (
            f"{city.title()}, {country.title()} - population {str(population)}"
        )
    else:
        city_country_formatted = f"{city.title()}, {country.title()}"

    return city_country_formatted


# print(city_function("rabat", "morocco"))
