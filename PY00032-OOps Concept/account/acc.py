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

    type = "Checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) #Calling init method of above classs
        self.fee = fee  #data member

    def transfer(self, amount): #class method here transfer is a method
        self.balance = self.balance- amount - self.fee

giri_checking = Checking("account\\giri.txt", 1) #Object instance
giri_checking.transfer(100)
print(giri_checking.balance)
giri_checking.commit()
    

teja_checking = Checking("account//teja.txt", 1) #Object instance
teja_checking.transfer(100)
print(teja_checking.balance)
teja_checking.commit()
    

print(giri_checking.__doc__)