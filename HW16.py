#Name:Tucker Hooper
#Class: 6th Hour
#Assignment: HW16


#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World")

#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
#4. Add a and b together, then divide the sum by c. Print the result.
sum=(a+b)
sum1=sum/c
print(sum1)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
ans=round(sum1,0)
print(ans)
if ans%2==0:
    print("Even")
else:
    print("Odd")
#6. Create a list of five different random integers between 1 and 10.
rand_list=[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
#7. Print the 4th number in the list.
print(rand_list)
print(rand_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
rand_list.append(random.randint(1,10))
print(rand_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
rand_list.sort(reverse=True)
print(rand_list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i < 100:
    i+= i
    print(i)

#11. Create a list containing the names of five other students in the classroom.
student_list = ["Matt" , "Owen", "Owyn","Misa","Nate"]
#12. Create a for loop that individually prints out the names of each student in the list.
for person in student_list:
    print(person)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
e = 1
for e in range(1 , 101):
    print(e)
    if e % 10 == 0:
        break
#14. Free space. Do something creative. :)
a = 1
while a <= 100:
    if a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    elif a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    else:
        print(a)
    a += 1