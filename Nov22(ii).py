correct_user="abcd987"
correct_password="asdf"
user_name=input("Enter a username: ")
if (correct_user==user_name):
    password=input("Enter a password: ")
    if (correct_password==password):
        print("Login successful")
    else:
        print("Login is unsuccessful")
else:
    print("Username isnt valid!")