#for loop
'''names=["sree","voshnu","krishna","sowmini"]
for name in names:
    print(name.upper())'''


#while loop
'''correct_pin="1704"
enter_pin=input("enter your pin :")

while enter_pin != correct_pin:
    enter_pin=input("enter your pin :")
print("your pin is correct")'''

#sample 2
'''students = input("enter number of students :")
imposter = "5"
while students != imposter:
    print("you can go in")
    students = input("enter number of students :")
print("you are out")'''


#time bomb
'''import time
tic=10
while tic > 0:
    print(f"{tic} seconds remaining")
    tic -=1
    time.sleep(1) #wait 1 second for each iteration
print("your are done BOOOOOOOM!!!")'''


#break statement
items=[]

while True:
    item=input("enter item (type 'done' when done):")
    if item.lower() == "done":
        break
    items.append(item)

print(items)

