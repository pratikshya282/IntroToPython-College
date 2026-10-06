#RELATIONAL OPERATORS

#Is equal to
number=int(input("Enter an integer number: "))
if number==5:
    print("Your number matched!")
else:
    print("Your number didn't match.")

#Not equal to
alphabet=input("Enter an alphabet: ")
if alphabet!="b":
    print("It's not a match!")
else:
    print("Please try again.")

#Greater than
value=float(input("Enter a number: "))
if value > 10:
    print("Your value is greater than 10.")
else:
    print("Your value is less than 10.")

#Less than
if 3 < 7:
    print("true")
else:
    print("false")

#Greater than or equal to
num1=5
num2=9
if num1>=num2:
    print("Number 1 is greater!")
else:
    print("Number 2 is greater!")

#Less than or equal to
if 6<=3:
    print("false")
else:
    print("true")