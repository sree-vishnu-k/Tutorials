'''name = " srEE Vishnu "
mobile =6383882727

#basic string handiling
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.lower().count("e"))
print(str(mobile)[:2]+"******"+str(mobile)[-2:])
print(name.replace(" ","_"))
print(str(mobile).split(" "))
print(name.strip())


#if and find in string handling
message="please call the student with a roll of 23cs261 immediately"
if "23cs261" in message:
    print(f"the roll is found as,{message.find("23cs261")} th position")'''


#for in string handling

name="sree vishnu"
initial="".join([word[0].upper() for word in name.split()])
print(initial)
print(len(initial))


