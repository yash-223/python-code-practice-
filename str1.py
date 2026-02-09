 # Write a program to iterate through a dictionary and print all keys.

student = {"name": "sakshi", "age": 23, "emailid": "sakshisali@gmail.com", "address":"aalandi"}

print(student.keys())


# Write a program to iterate through a dictionary and print all values.

student = {"name": "sakshi", "age": 23, "emailid": "sakshisali@gmail.com", "address":"aalandi"}

print(student.values())


# Write a program to add a new key-value pair to an existing dictionary.

student = {"name": "sakshi", "age": 23, "emailid": "sakshisali@gmail.com", "address":"aalandi"}

student["aadhar_no"] = 784773
print(student)

# Write a Python function that takes a dictionary and a key, and returns the value if the key exists, else "Key not found".

def get_value(data, key):
    return data.get(key, "Key not found")


student = {
    "name": "Sakshi Sali",
    "age": 20
}

print(get_value(student, "name"))
print(get_value(student, "city")) 


# Write a program to remove the "city" key from the dictionary person = {"name": "John", "age": 25, "city": "New York"} and print the resulting dictionary.

person = {"name": "John", "age": 25, "city": "New York"}

person.pop("city")
print(person)

# Write a Python program that inverts a dictionaryfruit_prices = { "apple": 50,"banana": 20,"orange": 30,"mango": 60,"grapes": 40} i.e., swaps keys with values.

fruit_prices = { "apple": 50,"banana": 20,"orange": 30,"mango": 60,"grapes": 40}

invented_by = {v:k for k,v in fruit_prices.items()}
print(invented_by) 

# Write a program that updates a dictionary student_marks = {"Alice": 85, "Bob": 72, "Charlie": 90,"David": 65,"Eva": 78}with another dictionary 
# students = {
#     "Alice": {"Math": 85, "Science": 90},
#     "Bob": {"Math": 70, "Science": 80},
#     "Charlie": {"Math": 95, "Science": 88}
# }


student_marks = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 78}

students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 70, "Science": 80},
    "Charlie": {"Math": 95, "Science": 88}
}


for name in students:
    student_marks[name] = students[name]
print(student_marks)

# 8. Write a program that merges two dictionaries dict1 = {"name": "John", "age": 25} and dict2 = {"city": "New York", "country": "USA"}.


dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "country": "USA"}


dict1.update(dict2)
print(dict1)

 # Write a program that iterates through the dictionary person = {"name": "John", "age": 25, "city": "New York"} and prints both the keys and values.

person = {"name": "John", "age": 25, "city": "New York"}

print(person.items())
print(person.keys())
print(person.values())

# Write a Python program that finds the key with the maximum value in a dictionary.

student_marks = {
    "yash" : 80,
    "sakshi" : 99,
    "vishal": 98,
    "guru": 90
}

max_key = max(student_marks,key=student_marks.get)

print("highest marks score by:", max_key)
print("Marks:", student_marks[max_key] )

# Write a program that creates a dictionary from a list of numbers, where the keys are the numbers, and the values are their squares.

numbers = [1, 2, 3, 4, 5]

squares = {}

for n in numbers:
    squares[n] = n ** 2

print(squares)


# Write a Python program that inverts a dictionary, i.e., swaps keys with values.

name = {
    "name": "sakshi" , "age": 23, "emailid": "sakshisali@gmail.com"
}

invented_by = {v:k for k,v in name.items() }
print(invented_by)


# fruit_prices = {"apple": 50, "banana": 20, "orange": 30, "mango": 60, "grapes": 40}

 # 1. Add a new fruit "pineapple": 70 to the dictionary.
 # 2. Update the price of "banana" to 25.
 # 3. Remove "orange" from the dictionary.
 # 4. Check if "apple" exists as a key in the dictionary.



fruit_prices = {"apple": 50, "banana": 20, "orange": 30, "mango": 60, "grapes": 40}

fruit_prices["pineapple"] = 70
print(fruit_prices)

updates[banana] = 25
