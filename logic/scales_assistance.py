from entity.toys import Toys
from container.tree import Tree


class ScalesAssistance:
    @staticmethod
    def calculate_total_price(tree):
        if isinstance(tree, Tree) and tree.size != 0:
            total = 0
            for i in range(tree.size):
                toys = tree.get_toys(i)

                if isinstance(toys, Toys):
                    total += toys.price

            return total
        else:
            return 0

    @staticmethod
    def calculate_total_weight(tree):
        if isinstance(tree, Tree) and tree.size != 0:
            total = 0
            for i in range(tree.size):
                toys = tree.get_toys(i)

                if isinstance(toys, Toys):
                    total += toys.weight

            return total
        else:
            return 0

