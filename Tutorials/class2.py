from Tutorials.class1 import Person

class student(Person): #child
    def greet(self):
        print("Welcome to student")

    def show(self):
        print(f"{self.age} is {self.name} years old")


person1 = student("sree", 20)
person1.show()
person1.greet()