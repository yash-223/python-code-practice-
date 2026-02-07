print("Welcome to ATM")

balance = 5000
pin = int(input("Enter PIN :"))
amount = int(input("Enter withdraw amount : "))

if pin == 1234:
    if amount <= balance:
       
        balance = balance - amount 
        
       
        print("allow withdraw :")
       
        print("current balance :", balance)
    else:
            print("influcient balance")
else:
    print("incorrect PIN ")
            
            
        