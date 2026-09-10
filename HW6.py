#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
numbers=[1, 7, 3, 5, 9, 13, 15, 11, 17]

print(numbers)
#2. Sort the list from highest to lowest.
numbers.sort(reverse=True)

print(numbers)
#3. Create an empty list.
mt=[]

print(mt)
#4. Remove the median number from the first list and add it to the second list.
num_sum=sum(numbers)
print(num_sum)
med=num_sum/9
print(med)
mt.insert(0,med)
print(mt)
#5. Remove the first number from the first list and add it to the second list.
num_pop=numbers.pop(0)
print(numbers)
mt.insert(1,num_pop)
print(mt)
#6. Print both lists.
print(numbers)
print(mt)
#7. Add the two numbers in the second list together and print the result.
mt_sum=(mt[0]+mt[1])
print(mt_sum)
#8. Add the sum from #7 to the first list.
numbers.append(mt_sum)
print(numbers)
#9. Sort the first list from lowest to highest and print it.
numbers.sort()
print(numbers)