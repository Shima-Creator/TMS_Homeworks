class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False,
                 mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon


class PizzaBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def set_cheese(self):
        self.cheese = True
        return self

    def set_pepperoni(self):
        self.pepperoni = True
        return self

    def set_mushrooms(self):
        self.mushrooms = True
        return self

    def set_onions(self):
        self.onions = True
        return self

    def set_bacon(self):
        self.bacon = True
        return self

    def get_pizza(self):
        return self.pizza

    def pizza_build(self):
        return Pizza(self.size, self.cheese, self.pepperoni,
                     self.mushrooms, self.onions, self.bacon)


class PizzaDirector:
    def __init__(self, pizza_builder):
        self.builder = pizza_builder

    def make_pizza(self, size, cheese=False, pepperoni=False,
                   mushrooms=False, onions=False, bacon=False):
        self.builder = PizzaBuilder(size)

        if cheese:
            self.builder.set_cheese()
        if pepperoni:
            self.builder.set_pepperoni()
        if mushrooms:
            self.builder.set_mushrooms()
        if onions:
            self.builder.set_onions()
        if bacon:
            self.builder.set_bacon()

        return self.builder.pizza_build()


director = PizzaDirector(PizzaBuilder("Big"))

first_pizza = director.make_pizza("Big", cheese=True, mushrooms=True,
                                  pepperoni=True, onions=True)
