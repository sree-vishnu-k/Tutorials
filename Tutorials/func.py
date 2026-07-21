# basic function
"""
def greet_1():
  print("good morning")

def greet_2():
    print("good afternoon")

def greet_3():
    print("good evening")

def greet_4():
    print("good night")

greet_1()
greet_2()
greet_3()
greet_4()


# function using return

def student(name,age):
    return f"the student name is,{name} \n and {age} years old"



# *args in functioms

def add(*args):
    return sum(args)
print(add(1,2,3,4,5,6))

def students(*args):
    return f"the following students are: {",".join(args)}"
print(students("sree","vishnu","krishna","sowmini"))
"""

#kwargs
def personal(**kwargs):
    print("|".join(f"{k}:{v}" for k,v in kwargs.items()))
personal(name="sree",age=20,role="student")