# 1.Create a string using single quote , double quotes and triple quotes and print it.


# 2.Count the number of occurrences of a specific character in a string.

str1 = "HEFSHINE SOFTWAER"
char = "E"
print(str1.count(char))



# 3.Write a program to count the number of words in a string.


text = "Yash sali"
count = len(text.split())
print(count)


# 4.Write a program to check if a string contains only digits.

print(str1.isdigit())

# 5.How can you sort the characters of a string alphabetically.

sorted(str1)
join = "".join(sorted(str1))
print(join)
# 6.Write a program to find whether a given string is a palindrome.
a = str1[::-1]
if str1 == a:
    print("its a palindrom")
else:
    print("its palindrom ")
   


# 7.Write a Python code to reverse the words in a sentence.
str_1 = "python is a interpreted language"

splited = str_1.split()
reversed_str = splited[::-1]
join = " ".join(reversed_str)
print(join)

# 8. Accept comma separated sequence of words as input and
#     print the words in sorted form (alphanumerically) 
# Sample Words : orange, red, white, black, green  
# Expected Result : black, green, orange, red, white 


words = "orange,red,white,black,green" 
split_words = words.split(",")
sorted_words = sorted(split_words)
join = ",".join(sorted_words)
print(join)
# 9. Write a program to swap comma and dot in a string.  
# Sample string: "47,89,56.3"  
# Expected Output: "47.89.56,3" 
# Assignments For Students-
sample_string  = "47,89,56.3"
print(sample_string.replace(".","@").replace(".",",").replace("@","."))



# 1.Replace all occurrences of a substring with another substring.
text1 = "hefshine sofwtwaer"
text2 = "yash sali"

print(text1.replace(text1,text2))
# 2.Check if the string starts with a given prefix or ends with a given suffix.

text = "Hello world"
print(text.startswith("Hello"))
print(text.endswithswith("world"))
# 3.Remove all whitespace from a string.

text1 = "     remove spaces         "
print(text1.strip())


# 4.Read a string. Exchange first and last character of a string. Display it.

text = "HeFShine"
first_char = text[0]
mid = text[1:-1]
last_char = text[-1]

print(last_char +  mid + first_char  )




# 5.Write a program to remove all spaces from a string in Python.
text = "yash sali erandol"
print(text.replace(" ",""))

# 6.Read a line from user. Print three strings using odd  indexed characters, even indexed characters and every third character.
text = "Hefshine solution "
odd = text[1::2]
print(odd)

text1 = "Hefshine solution "
even = text1[0::2]
print(even)

text3 = "Hefshine solution "
third_char = text1[::3]
print(third_char)

# 7. Write a Python program to check if a substring exists in a given string.

substring = "yash sali "
word = "yash"
if substring in word:
    print("True")
else:
    print("false")

# 8. Write a Python program to check if two strings are anagrams.
#      (contain  the same characters in a different order).

