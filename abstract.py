# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass

#     @abstractmethod
#     def movement(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return  "Woof"

#     def movement(self):
#         return "Walks on 4 legs"


# class Bird(Animal):
#     def speak(self):
#         return "Chirp"

#     def movement(self):
#         return "Flies in the sky"


# dog1 =Dog()
# print(dog1.speak())
# print(dog1.movement())

# bird1 = Bird()
# print(bird1.speak())
# print(bird1.movement())




# from abc import ABC, abstractmethod

# class Creature(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Cat(Creature):
#     def sound(self):
#         print("Meow")

# c = Cat()
# c.sound()


# from abc import ABC, abstractmethod

# class Creature(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Cat(Creature):
#     def sound(self):
#         print("Meow")

# c = Cat()
# c.sound()



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def sleep(self):   # concrete method
#         print("Sleeping")

#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# d = Dog()
# d.sleep()
# d.sound()




# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def draw(self,color,size):
#         pass

# class Circle(Shape):
#     def draw(self,color,size):
#         print(f"circle of color {color} and size {size}")

# c = Circle()
# c.draw("Red", 10)



# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * self.r

# class Square(Shape):
#     def __init__(self, s):
#         self.s = s

#     def area(self):
#         return self.s * self.s

# c = Circle(5)
# s = Square(4)

# print("Circle area:", c.area())
# print("Square area:", s.area())



# # 6.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass 

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return f"The area of the circle is: {3.14 *self.radius * self.radius **2}"

# class Square(Shape):
#     def __init__(self,side):
#         self.side =side















# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self,work_days pay_per_day):
#         self.work_days = work_days
#         self.pay_per_day= pay_per_day


#     def calculate_salary(self):










from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, initial_balance):
        self.balance = initial_balance
        print(f"Initial Bank Balance is: {self.balance}")

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Balance after deposit of {amount} is {self.balance}"
        else:
            return "Invalid amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Balance after withdrawal of {amount} is {self.balance}"
        else:
            return "Insufficient balance or invalid amount"


# Example usage
account = SavingsAccount(1000)
print(account.deposit(500))
print(account.withdraw(300))