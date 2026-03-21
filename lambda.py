numbers = [1,2,3,4,5,6,7,8,9]
result = list(map(lambda num: num**3, numbers))
print(result)



names = ["sakshi", "yash", "sagar", "muskan"]
result = list(filter(lambda name : name.startswith("s"),names))
print(result)


add_10 = lambda x : x+10
num = 5
print(add_10(num))


names1 = ["sakshi", "yash", "prasad"]
result = list(map(lambda x : x.upper(), names1))
print(result)


list1 = [1,2,3]
list2 = [4,5,6] 

result = list(map(lambda x,y: x+y, list1,list2))
print(result)


names2 = ["pranjal", "kavita", "mayuri"]
result = list(filter(lambda name: name.startswith("k"), names2))
print(result)



number = [1,10,12,13,15,2,3,5]
result = list(filter(lambda num: num>10, number))
print(result)


product = lambda a,b: a*b
print(product(5,10))


numbers = [1,2,33,4,55]
result = list(map(lambda x: x*2,numbers))
print(result)

even_number = [1,2,3,4,5,6,7,8,9]
result = list(filter(lambda x: x % 2 != 0, even_number))
print(result)


empty_string = ["sakshi", "", "yash", "", "arun",""]
result = list(filter(lambda x: x != "", empty_string))
print(result)

words = ["kiwi", "apple", "banana","cherry"]
result = sorted(words, key=lambda x: len(x))
print(result)

num = [123,456,789]
result = list(map(lambda x: x % 10, num ))
print(result)


words = ["pranjal", "kavita", "mayuri"]
result = max(words, key= lambda x: len(x))
print(result)

data = [(1,2),(2,3),(6,7),(5,6)]
result = sorted(data, key = lambda x: x[1])
print(result)



 