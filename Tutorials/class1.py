class Person: # parent
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old")

