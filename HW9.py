#Name: Tucker Hooper
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dict1={
    "brand" : "Lincoln",
    "model" : "Continental",
    "year" : [2017, 2018, 2019]
}
print(dict1)
#3. Print the keys of the dictionary from #2.
print(dict1.keys())
#4. Print the values of the dictionary from #2
print(dict1.values())
#5. Print one of the three numbers from the list by itself
print(dict1["year"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dict1.update({"trim" : "reserve"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(dict1)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
class_dict={
    "Owen" : {
        "Name" : "Owen",
        "Grade" : 12,
        "shower" : True,
    },
    "Matthew" : {
        "Name" : "Matt",
        "Grade" : 12,
        "shower" : False,
    },
    "Owyn" : {
        "Name" : "Owyn",
        "Grade" : 9,
        "shower" : False,
    },
}


#9. Print the names of all three classmates on the same line.
print(class_dict.keys())
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
class_dict.pop("Owyn")
print(class_dict)