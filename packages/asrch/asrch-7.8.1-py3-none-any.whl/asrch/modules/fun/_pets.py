from dataclasses import dataclass

from asrch.utils.constants import Colors

colors = Colors()


@dataclass
class Pet:
    age: int
    name: str
    health: int
    color: Colors

    @property
    def pet_name(self) -> str:
        return self.name

    @pet_name.setter
    def pet_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Error: Name must be a string")
        print(f"Name set: {value}")
        self.name = value


@dataclass
class Cat(Pet):
    character = "ᓚᘏᗢ"


@dataclass
class Dog(Pet):
    pass


@dataclass
class Bird(Pet):
    pass


@dataclass
class Monkey(Pet):
    character = "@('-')@"


my_cat = Cat(0, "", 0, Colors.NC)
my_cat.pet_name = "joe"
