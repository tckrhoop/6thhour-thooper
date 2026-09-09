#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
list= ["Owen", "Matthew", "Tucker", "Keith", "Ashton"]

print(list)
#2. Append a new name onto the Name List.
list.append("Stryker")
print(list)
#3. Print out the 4th name on the list.
print(list[0])
#4. Create a list with 4 different integers in it.
numbers=[72, 38 , 45, 63]

print(numbers)
#5. Insert a new integer into the 2nd spot and print the new list.
numbers.insert(1,13)

print(numbers)
#6. Sort the list from lowest to highest and print the sorted list.
numbers.sort()

print(numbers)
#7. Add the 1st three numbers on the sorted list together and print the sum.
numbers_sum=numbers[0]+numbers[1]+numbers[2]
print(numbers_sum)
#8. Create a list with two strings, two variables, and two boolean values.
mixed=["Steve", "Joe", 46, 65, True, False]

print(mixed)
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(mixed[int(input("Enter index value"))])