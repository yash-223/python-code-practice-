 #{}

Book = {
    "name" : "step to success",
    "color" : "black",
    "auther" : "sakshi sali",
    "invented_by" : 2025
}
print(Book)
     

student = dict([("name", "Sakshi Sali"), ("age", 20)])
print(student)

# Removing item 
# pop item

student = {"name": "Sakshi Sali", "age": 20, "city": "Pune"}

student.pop("age")
print(student)

# popitem

# data = {"a": 1, "b": 2, "c": 3}

# data.popitem()
# print(data)


data  = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
data.popitem()
# print(data)


# clear item 

data.clear()
print(data)

# del key

student = {"name": "Sakshi Sali", "age": 20}

del student["age"]
print(student)

# dict of copy

d1 = {"a": 1}
d2 = {"b":2}
d3 = d2.copy()
print(d3)

# Adding element 

student = {"name": "sakshi"}

student["city"] = "pune"
print(student)

# Accessing Items

student = {"name": "harsha", "age": 20}

# print(student["name"])
print(student.get("name"))

 # keys(), values(), items()

# name  = {"name":"yash", "age": 20, "emailid":"sakshi@gmail.com" }
# print(name.keys())

name = {"name":"yash", "age": 20, "emailid":"sakshi@gmail.com" }
print(name.values())


name = {"name":"yash", "age": 20, "emailid":"sakshi@gmail.com" }
print(name.items())

student = {"name": "Sakshi Sali", "age": 20}

del student["age"]
print(student)

# Update element 
student = {"name": "Sakshi Sali", "age": 20}

student["age"] = 21
print(student)


student = {"name": "sakshisali", "age": 22}

student["age"] = 23
print(student)

# nested dictionary 

family = {
    "child1": {
        "name": "sakshi",
        "age": 23,
        "education": "BE 3rd year"
    },

    "child2": {
        "name": "yash",
        "age": 21,
        "education": "BCA 3rd year"
    },

    "child3": {
        "name": "sayali",
        "age": 20,
        "education": "B.com"
    },

    "child4": {
        "name": "guru",
        "subject": {"python": 70, "java": 90, "c": [70, 90, 100]}
    }
}

# update name
family["child4"]["name"] = "kritika"

print(family)


