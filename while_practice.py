# num = int(input("Enter number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     i = 2
#     is_prime = True
    
#     while i <= num // 2:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1   
    
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")


# n = int(input("Enter a number"))

# a = 0
# b = 1 

# while a <=n:
#     print(a, end= " ")




num = int(input("Enter a number"))

reverse = 0
while num>0:
    digit = num % 10      
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse) 


x = int(input("Enter a number"))
n = int(input("Enter a number"))

result =1 
i =1 

while i<= n:
    result = result * x
    i += 1
print(result)







str = "listen"
words = ["silent", "enlist","listen","listen1","good"]
result = []

for word in words:
    if sorted(str)== sorted(word):
        result.append(word)
print(result) 


 











