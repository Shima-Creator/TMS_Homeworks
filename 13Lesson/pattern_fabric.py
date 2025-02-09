from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав-гав"


class Cat(Animal):
    def speak(self):
        return "Мяу-мяу"


class AnimalFactory:

    @staticmethod
    def create_animal(animal):
        animal = animal.lower()
        if animal == "dog":
            return Dog()
        elif animal == "cat":
            return Cat()
        else:
            raise ValueError("Введено неверное животное!")


factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
print(dog.speak())