import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """Do names like 'janis joplin' work?"""
        formatted_name = get_formatted_name("janis", "jolpin")
        self.assertEqual(formatted_name, "Janis Jolpin")


if __name__ == "__main__":
    unittest.main()
