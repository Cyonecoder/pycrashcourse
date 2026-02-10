import unittest
from city_function import city_function


class CitiesTestCase(unittest.TestCase):
    """test for city_function.py"""

    def test_city_name(self):
        city_result = city_function("rabat", "morocco")
        self.assertEqual(city_result, "Rabat, Morocco")


if __name__ == "__main__":

    unittest.main()
