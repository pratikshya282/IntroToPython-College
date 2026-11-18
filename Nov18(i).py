#Ask the user for two numbers as text input, convert both to int, and print their sum.
a=input("Enter a number: ")
b=input("Enter another number: ")
c=int(a)
d=int(b)
e=c+d
print(e)

#Take a float like 9.87 and print it as (a)a truncated int using int(), and (b)a rounded int using round().
#Compare the two results.
f=9.87
print(int(f))
print(round(f))
#int() function gives 9 and round () gives 10 as the output. The int() function removes the value after decimal
#point and displays only the value before the decimal. The round() function rounds-off the number into a whole num.

#Convert a list with duplicate numbers into a set, then back into a sorted list and print the result.
age=[2,5,7,9,7,15,21,9,11]
age_set=set(age)
age_list=list(age_set)
age_list.sort()
print(age_list)

#Predict the output of bool("False") before running it, then check your answer. Explain in your own words
#why it gives that result.
bool("False")