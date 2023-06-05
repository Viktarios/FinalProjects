from entity.ball import Ball
from entity.cone import Cone
from entity.snowflake import Snowflake
from container.tree import Tree
from logic.scales_assistance import ScalesAssistance


def main():
    tree = Tree()

    toy1 = Ball("white", "large", 55, 210)
    toy2 = Ball("red", "middle", 36, 170)
    toy3 = Cone("yellow", "small", 25,120)
    toy4 = Cone("orange", "large", 43, 190)
    toy5 = Snowflake("blue", "middle", 33, 150)
    toy6 = Snowflake("purple", "small", 30, 140)

    tree.add(toy1)
    tree.add(toy2)
    tree.add(toy3)
    tree.add(toy4)
    tree.add(toy5)
    tree.add(toy6)

    print(tree)

    price = ScalesAssistance.calculate_total_price(tree)
    weight = ScalesAssistance.calculate_total_weight(tree)

    print(f"Total price is ${price}")
    print(f"Total weight is {weight}gr")


if __name__ == "__main__":
    main()
