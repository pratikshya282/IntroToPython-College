#LOGICAL OPERATORS

#and
age=int(input("Enter your age: "))
license=input("Do you have a driving license (Yes/No): ")
if age>=18 and license=="Yes":
    print("You can drive!")
else:
    print("You are not eligible for driving!")

#or
coupon=input("Do you have a coupon (Y/N): ")
qr=input("Do you have the qr code (Y/N): ")
if coupon=="Y" or qr=="Y":
    print("You win $5!")
else:
    print("Please buy a ticket!")

#not
pas=40
user_mark=float(input("Enter your marks: "))
if not user_mark == pas:
    print("Pass")
else:
    ("Fail")