from abc import ABC, abstractmethod
from unicodedata import name
from unicodedata import name

class Animal(ABC):

    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display(self):
        print(f"{self.name} lives in {self.habitat}.")
        
    @abstractmethod
    def make_sound(self):  
        pass

class Dog(Animal):

    def __init__(self, name, habitat):
        super().__init__(name, habitat)

    def make_sound(self):
        print(f"{self.name} barks: Woof! Woof!")

class Cat(Animal):

    def __init__(self, name, habitat):
        super().__init__(name, habitat)

    def make_sound(self):
        print(f"{self.name} meows: Meow! Meow!")

class Cow(Animal):

    def __init__(self, name, habitat):
        super().__init__(name, habitat)

    def make_sound(self):
        print(f"{self.name} moos: Moo! Moo!")

dog = Dog("Buddy", "House")
cat = Cat("Whiskers", "House")  
cow = Cow("Bessie", "Farm")

print("Animal Sound Show:")
for animal in [dog, cat, cow]:
    animal.display()
    animal.make_sound()
    print()