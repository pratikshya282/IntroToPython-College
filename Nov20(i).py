#ask user for full name and print first letter of each word capitalised
full_name=input("Enter your full name: ")
print(full_name.title())

#print a word reversed using slicing
given_word="apple"
print(given_word[::-1])

#take sentence as user input and use .count() to print how many times letter "e" is there.
sentence=input("Enter a sentence: ")
e_count=sentence.count("e")
print(e_count)

#take a sentence & use .split() and .join() to print sentence with words in reverse.
a="The apple is sweet ."
splitt=a.split()
reverse=splitt[::-1]
joined="".join(reverse)
print(joined)

#Check wheather the word is palindrome or not.
palindrome_word=input("Enter a word: ")
reversing=(palindrome_word[::-1])
if palindrome_word==reversing:
    print("Word is palindrome!")
else:
    print("Not palindrome!")

#Create a formatted receipt line using python f-string.
fruit_name="banana"
fruit_quantity=4
fruit_price=9.51
print(f"Total price for {fruit_name} of {fruit_quantity} quantity is of ${fruit_price}.")