from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Person:

    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name}, {self.job} ({self.age})'

# -----------------------------------------------------

# initialises data classes
person1 = Person("Alex", "Programmer", 18, 99)
person2 = Person("Dave", "None", 33)

# prints id of data classes
print(id(person1))
print(id(person2))

# calls __str__ method of data class, otherwise prints memory address
print(person1)

# prints whether person1 is stronger as data class is ordered by strength
print(person1>person2)
