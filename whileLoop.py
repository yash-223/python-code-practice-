# # i = 1

# # while i<=10:
# #     print(i)
# #     i+=1


# # i = 50

# # while i>= 1:
# #     print(i)
# #     i-=1


# # num = 1 
 
# # while num<= 50:
# #     print(num)
# #     num += 2

# num1 = 2

# while num1<= 50:
#     print(num1)
#     num1 += 2

# lst = [1, 3.4, 56, "Sagar", "Pune", ["a", "b", "c"], True]

# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1




# numbers = [10, 20, 30, 40, 50]

# total = 0
# i = 0

# while i < len(numbers):
#     total += numbers[i]
#     i += 1

# print("Sum =", total)



# num = 1
# total = 0

# while num <= 1000:
#     total += num
#     num += 1

# print("Sum =", total)



# n = 5
# fact = 1
# i = 1

# while i <= n:
#     fact *= i
#     i += 1

# print("Factorial =", fact)


# num = 12345
# count = 0

# while num > 0:
#     num //= 10
#     count += 1

# print("Digits =", count)



# num = 12345
# total = 0

# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10

# print("Sum of digits =", total)



# # Write a program to seperate and to store even or odd into two different list.

# numbers = [10, 15, 22, 33, 40, 55, 62, 71]

# even_list = []
# odd_list = []

# # initialize index
# i = 0

# # while loop
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         even_list.append(numbers[i])
#     else:
#         odd_list.append(numbers[i])
    
#     i += 1


# print("Original list:", numbers)
# print("Even list:", even_list)
# print("Odd list:", odd_list)


# # Write a program to seperate and to store vowels and consonants into two different list.

# # Program to separate vowels and consonants using while loop

text = input("Enter a string: ")

vowels = []
consonants = []

i = 0

while i < len(text):
    ch = text[i].lower()
    
    if ch.isalpha():   
        if ch in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(ch)
        else:
            consonants.append(ch)
    
    i += 1

print("Vowels list:", vowels)
print("Consonants list:", consonants)  


n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n*i)


#write a python program

text = input("Enter string: ")
char = input("Enter character to count: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("Count is:", count)


# 
str = input("enter a string")
count = 0

for i in str:
    if i == "AEIOUaeiou":
        count+1


print(count)



