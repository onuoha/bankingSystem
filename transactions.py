#OOPL Task: Banking System using OOP

#Parent Class: User
#- Holds details about a user
#- Has a function to show user details
#Child Class: Bank
#- Stores details about the account balance
#- Stores details about the amount 
#- Allows for deposits withdraw, view_balance etc.

# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_details(self):  # self makes it possible for this function to have access to all properties in every method assigned to this object
        print('Personal Details')
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)

# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Amount deposited: ", self.amount, "Account balance: ", self.balance)

    
    def withdrawal(self, w_amount):
        self.amount = w_amount
        if self.amount > self.balance:
            print("Insufficient Balance | Balance: ", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Amount withdrawn: ", self.amount, "Account balance: ", self.balance)
    
    def view_balance(self):
        self.show_details()
        print("Hallo", self.name, " your account balance is: ", self.balance)




user1 = User('Pat', 30, 'female')
#print(user1.show_details())
user2 = Bank('Roy', 35, 'male')
print(user2.age)
user3 = Bank('Femi', 34, 'female')
user2.deposit(100)
user3.deposit(300)
user2.deposit(50)
user3.deposit(72)
user2.withdrawal(55)
user3.withdrawal(300)
user2.withdrawal(100)
user2.view_balance()
user2.withdrawal(80)
user2.view_balance()
