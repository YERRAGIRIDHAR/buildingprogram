class Account:

    '''Craeting the constructor'''

    def __init__(self, filepath):
        self.filepath = filepath #Instance variable
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    '''Craeting a withdraw function'''
    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    '''Craeting a deposite function'''
    def deposite(self, amount):
        self.balance = self.balance + amount

    '''writing into the file'''
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


# account=Account('account//balance.txt')
# print(account.balance)
# account.deposit(500)
# print(account.balance)
# account.commit()


'''Creating inheritance'''
class Checking(Account): 

    """This class Generates checking account objects"""

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) #Calling init method of above classs
        self.fee = fee  #data member

    def transfer(self, amount): #class method here transfer is a method
        self.balance = self.balance-amount-self.fee

Giri_checking = Checking("account\\Giri.txt", 1) #Object instance
Giri_checking.transfer(1200)
print(Giri_checking.balance)
Giri_checking.commit()
    

Teja_checking = Checking("account\\Teja.txt", 1) #Object instance
Teja_checking.transfer(1200)
print(Teja_checking.balance)
Teja_checking.commit()
    