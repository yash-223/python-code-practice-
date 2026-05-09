# #1 Write a program to print the first character of a string.?\
#     #01234567
# a = "HEFSHINE"
# first_string = a[0]
# print(first_string)

# #2 Given a string, print its last character using negative indexing.

# print(a[-1])


# #3 Extract and print the first 5 characters of a string.

# print(a[:5])

# #4 Write a program to reverse a string using slicing.

# print(a[::-1])

# #5 Print every second character from the string using slicing.

# print(a[1])

# #6 Print the first and last character of the string using indexing.

# first_char = a[0]
# last_char = a[-1]
# print(first_char + last_char)

# #7 Extract and print everything except the first and last characters.

# print(a[1:-1])

# #8 Write a program that prints the character at the middle index of the string.

# text = "meansftgyrgh"
# middel = len(text) // 2   
# print(text[middel])

# #9  Divide a string into two halves and print both.

# t = input("Enter a string : ")

# mid = len(t) // 2

# first_half = t[:mid]
# second_half = t[mid:]

# print("first_half  : ", first_half)
# print("second_ half : ", second_half)


# #10 Replace the first character of a string with "@", keeping the rest unchanged.

# result = "@" + a[1:]


# #11 Print every 3rd character starting from index 0.


# print(a[:3])

#12 Write a function to check if a string is a palindrome using slicing.     
def is_palindrome(a):
    return a == a[::-1]

print(is_palindrome("madam"))