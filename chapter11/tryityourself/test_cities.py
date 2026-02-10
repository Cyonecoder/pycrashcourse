import unittest
from city_function import city_function


class CitiesTestCase(unittest.TestCase):
    """test for city_function.py"""

    def test_city_name(self):
        city_result = city_function("rabat", "morocco")
        self.assertEqual(city_result, "Rabat, Morocco")

    def test_city_country_population(self):
        city_result = city_function("rabat", "morocco", 3_000_000)
        self.assertEqual(city_result, "Rabat, Morocco - population 3000000")


if __name__ == "__main__":

    unittest.main()
