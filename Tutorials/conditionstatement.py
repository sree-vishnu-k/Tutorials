# sample conditional statement

'''age = int(input("enter your age:"))

if age >= 18:
    has_license = input("enter your licence status yes/no:")
    if has_license == "yes":
        print("You can drive")
    else:
        print("Take licence")
else:
    print("You are too young")'''

# test 1

has_membership=input("enter your membership status yes/no:").lower()
bill_ammount=int(input("enter your billing amount:"))
dayofweek=input("enter your dayofweek:").lower()

if has_membership == "yes" or bill_ammount >= 1000 and dayofweek in ["saturday","sunday"]:
    discount_amount=bill_ammount*0.20
    price =bill_ammount-discount_amount
    print(f"your discount is: ${discount_amount} and \nyour total payment ammount is: ${price}")
else:
    print(f"you have no discount \nYour total payment ammount is: ${bill_ammount}")
