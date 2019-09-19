class Account():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        print(f'Successfully created a new account for {self.owner} with an initial deposit of ${self.balance}.')
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'Successfully deposited ${amount}. Your new balance is ${self.balance}.')
        
    def withdraw(self,amount):
        if self.balance < amount:
            print(f'Your account balance is lower than ${amount}')
        else:
            self.balance = self.balance - amount
            print(f'Successfully withdrew ${amount}. Your new balance is ${self.balance}.')
    
    def __str__(self):
        return f"{self.owner}'s account has a balance of ${self.balance}."
    
# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)