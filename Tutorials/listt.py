"""
# creating list
cars=["Mercedes","ferrari","bmw","tata","audi"]
ranks=[1,2,3,4,5]

#printing list
for car,rank in zip(cars,ranks):
    print(f"{car} is {rank}")
#methods
cars.append("aston martin")
print(cars)
print(ranks)
ranks.insert(3,6)
print(cars)
print(ranks)
cars.remove("aston martin")
print(cars)
print(ranks)
cars.sort()
print(cars)
print(ranks)
cars.reverse()
print(cars)
print(ranks)
cars.pop()
print(cars)
print(ranks)
cars.clear()
print(cars)
print(ranks)
print(ranks[1:5])
"""
numbers=["1",2,3,4,5]
for i,number in enumerate(numbers):
    print(i,":",number)
print(numbers.count(5))

students = ["Sree", "Vishnu", "Krishna"]
marks = [90, 85, 95]

for index, (student, mark) in enumerate(zip(students, marks), start=1):
    print(index, student, mark)