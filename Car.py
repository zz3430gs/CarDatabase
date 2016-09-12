class Car:
    def __init__(self, make, year, model, price):
        self.make = make
        self.year = year
        self.model = model
        self.price = price

    def __repr__(self):
        self.str_repr = self.make + ' \t ' + self.year + ' \t ' + self.model + ' \t ' + self.price
        return self.str_repr