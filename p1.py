m1 = int(input("Enter a english marks : "))
m2 = int(input("Enter a math marks : "))
m3 = int(input("Enter a science marks : "))

total = ((m1 + m2 + m3) * 100) / 300 

if(total> 33 ):
    print("you are pass ")
else :
    print("you are fail ")



print("your percentage ", total )


