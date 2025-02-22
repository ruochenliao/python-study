from Animal import Animal


class Bird(Animal):
    def __init__(self, name, age, color, weight, height):
        super().__init__(name, age)
        self.color = color
        self.weight = weight
        self.height = height
        self.__max_price = 1000

    def set_max_price(self, max_price):
        self.__max_price = max_price

    def _set_private_variable(self):
        self._private_variable = "private variable"

    def _get_private_variable(self):
        return self._private_variable

    def make_sound(self, sound):
        print(self.name + " " + sound)


if __name__ == "__main__":
    bird = Bird("bird", 2, "blue", 1, 2)
    print(bird.name)
    print(bird.age)
    print(bird.color)
    print(bird.weight)
    print(bird.height)
    print(bird._get_private_variable())
    bird.make_sound("ji ji zha zha")
