#Ways of using print() function

name=input("Enter name: ")
#comma-seperated
print("Hello",name,"!")

location=input("Enter your location: ")
#concated
print("Hello"+name+"You live in"+location)

age=int(input("Enter your age: "))
#f-string method
print(f"Your age is {age}.")

#formatted method
print("Your name is {0} live in {1}".format(name,location))