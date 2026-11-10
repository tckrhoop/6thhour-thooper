#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: HW15


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.

for a in range(5,0,-1):
    print(a)
else:
    print("Hello World")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for b in range(1,31):
    if b%2==0:
        print(b)
    else:
        continue

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for c in range(1,31):
    if c % 3 == 0:
        continue
    else:
        print(c)

#4. Create a for loop that prints 5 different animals from a list.
animal_list = ["Jaguar", "Fishing cat", "Lion", "Kitty", "Tiger"]
for animal in animal_list:
    print(animal)

#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
d = (input("Enter a word: "))
e = ''
for Owen in d:
    e = Owen + e
print(e)

#6. Create a list containing 10 integers of your choice and print the list.
numlist  = [1,2,3,4,5,6,7,8,9,10]
print(numlist)
#7. Create two empty variables named evenNumbers and oddNumbers.
even_numbers = []
odd_numbers = []

#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for number in numlist:
    if number % 2 == 0:
        even_numbers.append(number)
    else: odd_numbers.append(number)
    continue
print(even_numbers)
print(odd_numbers)

import math

#9. Create a variable that asks the user for an integer and an empty integer variable.
f = int(input("Enter a number: "))
g = 0
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for i in range(g,f+1):
    factorial = math.factorial(i)
    print(factorial)