import unittest
from entity.toys import Toys


class ToysTest(unittest.TestCase):
    def test_price_property_positive(self):
        toys = Toys()
        expected_price = 1
        toys.price = 1

        self.assertEqual(expected_price, toys.price)

    def test_price_property_negative(self):
        toys = Toys()
        expected_price = -1
        toys.price = -1
        self.assertEqual(expected_price, toys.price)

    def test_price_property_with_zero(self):
        toys = Toys()
        expected_price = 0
        toys.price = 0
        self.assertEqual(expected_price, toys.price)

    def test_weight_property_positive(self):
        toys = Toys()
        expected_weight = 1
        toys.weight = 1

        self.assertEqual(expected_weight, toys.weight)

    def test_weight_property_negative(self):
        toys = Toys()
        expected_weight = -1
        toys.weight = -1
        self.assertEqual(expected_weight, toys.weight)

    def test_weight_property_with_zero(self):
        toys = Toys()
        expected_weight = 0
        toys.weight = 0
        self.assertEqual(expected_weight, toys.weight)

    def test_orange_constructor_with_args(self):
        expected_price = 1
        expected_weight = 1
        toys = Toys(expected_price, expected_weight)
        self.assertEqual(expected_price, toys.price)
        self.assertEqual(expected_weight, toys.weight)


if __name__ == "__main__":
    unittest.main()
