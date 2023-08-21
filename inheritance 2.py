class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def year(self):
        raise NotImplementedError("Child class must implement this method")


class Car1(Vehicle):
    def year(self):
        return 2013


class Car2(Vehicle):
    def year(self):
        return 2014


class Car3(Vehicle):
    def year(self):
        return 2015


car1 = Car1('Nissan', 'Altima')
print(car1.brand)
print(car1.model)
print(car1.year())

car2 = Car2('Toyota', 'Camry')
print(car2.brand)
print(car2.model)
print(car2.year())

car3 = Car3('Audi', 'Volvo')
print(car3.brand)
print(car3.model)
print(car3.year())