start=int(input("Enter starting range: "))
end=int(input("Enter starting range: "))
odd_count=0
even_count=0
for n in range(start, end+1):
    if (n%2 ==0):
        print(n,"even")
        even_count+=1
    else:
        print(n,"odd")
        odd_count+=1
print(f"ODD={odd_count}")
print(f"EVEN={even_count}")