from entity.toys import Toys

class Snowflake(Toys):
    def __init__(self, color='blue', size='small',price=0, weight=0):
        super().__init__(price,weight)
        self.__color = color
        self.__size = size


    @property
    def color(self):
        return self.__color

    @property
    def size(self):
        return self.__size

    @color.setter
    def color(self, color):
        self.__color = color

    @size.setter
    def flour(self, size):
        self.__size = size

    def __str__(self):
        return (f"Snowflake: color = {self.__color}, "
                f"size = {self.__size}, "
                f"price = {self.price}, "
                f"weight = {self.weight}")