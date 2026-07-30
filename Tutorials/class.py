class Person: # parent
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} years old")

class student(Person): #child
    def greet(self):
        print("Welcome to student")

    def show(self):
        print(f"{self.age} is {self.name} years old")


person1 = student("sree", 20)
person1.show()
person1.greet()