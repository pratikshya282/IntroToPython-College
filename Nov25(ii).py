length=int(input("Enter length of number: "))
odd_count=0
even_count=0
for n in range(length):
    num=int(input("Enter a number: "))
    if (num%2 ==0):
        print(num,"even")
        even_count+=1
    else:
        print(num,"odd")
        odd_count+=1
print(f"ODD={odd_count}")
print(f"EVEN={even_count}")