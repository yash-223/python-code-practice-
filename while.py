# # num = 2

# # while num <= 100:
# #     is_prime = True
# #     i = 2

# #     while i <= num // 2:
# #         if num % i == 0:
# #             is_prime = False
# #             break
# #         i += 1

# #     if is_prime:
# #         print(num)

# #     num += 1


# num =2 

# while num<=100:
#     is_prime = True
#     i = 2

#     while  i<=2 num//2:
#         if num % i ==0:
#             is_prime = False
#             break

#             i+= 1

#             if is_prime:
#                 print(num)

#                 num += 1
   
# r = 6 
# for i in range(r):
#     for j in range(i):
#    print( "*" ,end=" ")
#    print()


# n = 5
# for i in range (n):
#     for j in range (n):
#         if(j==0 or i==0 or i==2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         print()
            


# n = 5
# for i in range(n):
#     for j in range (n):
#         if(i==2 or )



lst1 = ["sakshi", "yash", 1, 2, 3]
lst2 = ["priya", "sakshi", 1, 2, 3, "yash"]

common_elements = []   # list define keli

for i in lst1:
    for j in lst2:
        if i == j:
            common_elements.append(i)

print(common_elements)




w = "listen"
words=["silent","stenli","enlist","good","istenl","listen"]
result= []

for word in words:
    if sorted(word)==sorted(w):
        result.append(word)

print(result)






 







