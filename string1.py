
''' you can check range hoy many charchter in your string '''

a = "Yash"
print(len(a))


'''upper() 
The upper() method converts a string to upper case.'''

str1 = "Harry"
print(str1.upper())




str1 = "HaRry"
print(str1.lower())


'''strip():
    strip() Python ka string function [ hai jo left + right dono side se extra spaces ] ya given characters hata deta hai.'''
    
str1 = "yash salli"
print(str1)

'''
rstrip()
the remove any traling charechter '''

str1 = "yash*******"
print(str1.rstrip("*"))

#  replace()
# The replace() method replaces all occurences of a string with another
# string . example 
    
str1 = "i love you"
print(str1.replace("love" , "hate"))

# split()
# the saperate string means break a string

str1 = "i love python"
print(str1.split())

# capitalize()
# capitalize  use for first heading charchter capital

str1 = "introduction your Self"
print(str1.capitalize())

# center()
# the center() method aligns the string to the center as per the parameter 
# given bythe user

str1 = "string in python"
print(str1.center(50))


# count()
# count charachter in strin ! its count repeat charechter

str2 = "asdfghgfdsaa"
print(str2.count("g"))


# endswith()
# the endswith() method check if the string ends with given value. if ye then return true,else return false

str1 = "welcome to the console!"
print(str1.endswith("!"))
print(str1.endswith("the",4,14))
print(len(str2))

# find()
# The final() method searches for the first occurences of the given value and return the index where it is present. it given value is absent from the string then return -1.

str1 = "he's name is"
print(str1.find("is"))
print(len(str1))

# index()

str1 = "he's name is"
print(str1.index("is"))
# isalnum();
# Ye check karta hai ki string me sirf alphabets (A–Z, a–z) aur numbers (0–9) hain ya nahi.
# 👉 Space, symbols (@, #, _, space) honge to False dega

str1 = "WelcomeToTheCo0nsole"
print(str1.isalnum())

# isaplha
# 👉 Ye check karta hai ki string me sirf alphabets (A–Z, a–z) hain ya nahi.
# 👉 Number, space, ya special character aaya to False dega.

str1 = "welcometotheconsole"
print(str1.isalpha())

# islower()
# THe islowe() method returns True if all the charechters in the string are lower case , ekse it return false.

str1 = "yashsakusn "
print(str1.islower())

# isprintable():
# The is printable() method returns True if all the values within the given string are printable if not then return false

str1 = "yash sali"   #true
print(str1.isprintable())



str1 = "yash \n 'ssali"    #false
print(str1.isprintable())

# isspace();
# the isspace() method returns trueonly and only if the sring contains white spaces,else return false

str1 = "     "
print(str1.isspace())

str2 = "   "
print(str2.isspace())

# istitle()
# The istitle() returns true only if the first letter of each word of the string is capitalize, else it returns false.
# Ye check karta hai ki string Title Case me hai ya nahi.

str1 = "Hello World "
print(str1.istitle())


# Swapcase()
# ye capital letter ko small karta hain or small ko capital

str1 = "yash sali "
print(str1.swapcase())

# title():
# the title() method capialize each letter of the words whithin the string

str1 = "he's name id Dan.Dan is an honest man"
print(str1.title() )




