import unittest

from container.tree import Tree
from entity.toys import Toys
from logic.scales_assistance import ScalesAssistance


class ScalesAssistanceTest(unittest.TestCase):
    def test_different_type_price(self):
        tree = "string"
        expected = 0

        actual = ScalesAssistance.calculate_total_price(tree)

        self.assertEqual(expected, actual)

    def test_different_type_weight(self):
        tree = "string"
        expected = 0

        actual = ScalesAssistance.calculate_total_weight(tree)

        self.assertEqual(expected, actual)

    def test_empty_tree_price(self):
        tree = Tree()
        expected = 0

        actual = ScalesAssistance.calculate_total_price(tree)

        self.assertEqual(expected, actual)

    def test_empty_tree_weight(self):
        tree = Tree()
        expected = 0

        actual = ScalesAssistance.calculate_total_weight(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_None_price(self):
        tree = None
        expected = 0

        actual = ScalesAssistance.calculate_total_price(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_None_weight(self):
        tree = None
        expected = 0

        actual = ScalesAssistance.calculate_total_weight(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_toys_positive_price(self):
        toy1 = Toys(5)
        toy2 = Toys(10)
        toy3 = Toys(5)

        tree = Tree()
        tree.add(toy1)
        tree.add(toy2)
        tree.add(toy3)

        expected = 20

        actual = ScalesAssistance.calculate_total_price(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_toys_positive_weight(self):
        toy1 = Toys(5, 5)
        toy2 = Toys(10, 4)
        toy3 = Toys(5, 6)

        tree = Tree()
        tree.add(toy1)
        tree.add(toy2)
        tree.add(toy3)

        expected = 15

        actual = ScalesAssistance.calculate_total_weight(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_one_toy_price(self):
        toy = Toys(5)

        tree = Tree()
        tree.add(toy)

        expected = toy.price

        actual = ScalesAssistance.calculate_total_price(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_one_toy_weight(self):
        toy = Toys(5)

        tree = Tree()
        tree.add(toy)

        expected = toy.weight

        actual = ScalesAssistance.calculate_total_weight(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_toys_positive(self):
        toy1 = Toys(5)
        toy2 = Toys(10)
        toy3 = Toys(2)

        tree = Tree()
        tree.add(toy1)
        tree.add("string")
        tree.add(toy2)
        tree.add(5)
        tree.add(toy3)

        expected = 17

        actual = ScalesAssistance.calculate_total_price(tree)

        self.assertEqual(expected, actual)

    def test_tree_with_toys_positive_weight(self):
        toy1 = Toys(5, 7)
        toy2 = Toys(10, 10)
        toy3 = Toys(2, 3)

        tree = Tree()
        tree.add(toy1)
        tree.add("string")
        tree.add(toy2)
        tree.add(5)
        tree.add(toy3)

        expected = 20

        actual = ScalesAssistance.calculate_total_weight(tree)

        self.assertEqual(expected, actual)


if __name__=="__main__":
    unittest.main()
