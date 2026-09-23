#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: HW8
import random

#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
a=random.randint(1,10)
b=random.randint(1,10)
c=random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(a,b,c)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
a2=a+2
b4=b-4
xc=c*1.5
#6. Print each result from #5 on the same line.
print(a2,b4,xc)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
intlist=[random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),]
print(intlist)
#8. Sort the list in #7 and print it.
intlist.sort()
print(intlist)
#9. Add together the highest three numbers in the list from #7 and print the result.
intadd=(intlist[2]+intlist[3]+intlist[4])
print(intadd)

#10. Create a list with 5 names of other students in this class and print the list.
namelist=["Matt","Owen","Owyn","Misa","Braylee"]
print(namelist)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(namelist)
print(namelist)
#12. Print a random choice from the list of names from #10.
class_num_choice = random.choice(namelist)
print(class_num_choice)
