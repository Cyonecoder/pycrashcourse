import unittest

from employe import Employee


class TestEmploye(unittest.TestCase):

    def setUp(self):

        self.employe = Employee("simo", "khass", 550_000)

    def test_give_default_raise(self):
        self.employe.give_raise()
        self.assertTrue(self.employe.annual_salary == 555000)

    def test_give_custom_raise(self):
        self.employe.give_raise(100000)
        self.assertTrue(self.employe.annual_salary == 650000)


if __name__ == "__main__":
    unittest.main()
