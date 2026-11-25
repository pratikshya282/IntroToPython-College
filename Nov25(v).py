for i in range(1,20+1):
    print(i)

for n in range(16):
    if (n%2 ==0):
        print(n,"even")

name="Pratikshya"
for m in range(7):
    print(name)
print("Done!")

n=int(input("Enter a number: "))
sum=1
for i in range(n+1):
    sum+=i
print(sum)

num=9
for i in range(1,11):
    print("9*",i,"=",9*i)

word=input("Enter a word: ")
vowel_count=0
for i in word:
    if i.lower() in "aeiou":
        vowel_count+=1
print(f"Vowel count={vowel_count}")

import time
timer_count=10
timing=0
for n in range(timer_count,timing,-1):
    print(n)
    time.sleep(1)

number=6
factorial=1
for i in range(1,number+1):
    factorial*=i
print(factorial)