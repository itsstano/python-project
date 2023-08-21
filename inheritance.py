class Animal:
    def __init__(self, name,color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Child classes must implement this method")


class Dog(Animal):
    def speak(self):
        return "woof!"


class Cat(Animal):
    def speak(self):
        return "Meows"

class Bird(Animal):
    def speak(self):
        return "Chirps"



# create an object
dog = Dog('Tom','Brown')
print(dog.name)
print(dog.color)
print(dog.speak())

cat = Cat('Lila','White')
print(cat.name)
print(cat.color)
print(cat.speak())

bird=Bird('Rio','Blue')
print(bird.name)
print(bird.color)
print(bird.speak())