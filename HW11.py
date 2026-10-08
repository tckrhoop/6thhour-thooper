#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
list= [random.randint(1,100),random.randint(1,100),random.randint(1,100)]

#3. Print the list.
print(list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if list[0]>list[1] and list[0]>list[2] :
    print("First is highest")
    num=list[0]
elif list[1]>list[0] and list[1]>list[2] :
    print("Second is highest")
    num=list[1]
else :
    print("Third is highest")
    num=list[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
print(num)
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num %2 == 0:
    print("num is divisible by 2")
elif num %3 == 0:
    print("num is divisible by 3")
elif num %2 == 0 and num %3 == 0:
    print("num is divisible by both")
else: print("num is not divisible by either")
