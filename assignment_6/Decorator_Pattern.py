class Pizza:
    def __init__(self):
        self.price = 10  

    def get_price(self):
        return self.price

class PizzaDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza  

    def get_price(self):
        return self._pizza.get_price()

class PepperoniTopping(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 2 

    def get_price(self):
        return self._pizza.get_price() + self.price

class MushroomTopping(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.price = 1.5  

    def get_price(self):
        return self._pizza.get_price() + self.price

basic_pizza = Pizza()

pizza_with_toppings = PepperoniTopping(MushroomTopping(basic_pizza))

print("Final price of the pizza with toppings:", pizza_with_toppings.get_price())
