from entity.toys import Toys


class Tree:
    def __init__(self, toys=None):
        if toys:
            self.__toys = toys
        else:
            self.__toys = []

    @property
    def size(self):
        return len(self.__toys)

    def get_toys(self, index):
        if (isinstance(index, int)
                and index >= 0 and index < self.size):
            return self.__toys[index]

    def add(self, toys):
        if isinstance(toys, Toys):
            self.__toys.append(toys)

    def __str__(self):
        msg = "List of toys:"

        for i in range(self.size):
            msg += f"\n{i + 1}) " + str(self.__toys[i])

        return msg