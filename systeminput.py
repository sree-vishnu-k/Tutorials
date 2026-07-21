import sys #importing system sys

#condition to avoid insufficient input
if len(sys.argv)<6:
    print("the arguments are: first name last name give both values")
    sys.exit()

first_name = " ".join(sys.argv[1]) #allocating system argument
last_name = " ".join(sys.argv[2]) #allocating 2nd argument
address = ",".join(sys.argv[3:]) #allocating 3rd argument

email = first_name.lower().replace(" ","")+"."+last_name.lower().replace(" ",".")+"@sriramcof.com" #calling name and giving it email version

#Output
print("\n --- Your profile ---")
print("Your name is ",first_name + "." + last_name.replace(" ",".")+".")
print("Your email is ",email)
print("Your address is ",address+".")