# enumerate function 

fruits = ["apple", "banana","cherry"]
for i , fruit in enumerate(fruits):
    print(i, fruit)

# enumerate with custom start index 

fruits = ["apple", "banana","cherry"]
for i , fruit in enumerate(fruits, start=1):
    print(i, fruit)

