class Person(object):

    def __init__(self, first_name, last_name, age):         # default constructor
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    @classmethod
    def from_full_name(cls, name, age):                     # "factory" method
        if " " not in name:
            raise ValueError("Only first name or last name entered.")
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")


def main():
    person0 = Person("Person", "Zero", 0)
    person1 = Person.from_full_name("PersonOne", 1)

    person0.greet()
    person1.greet()


if __name__ == "__main__":
    main()
