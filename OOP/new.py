import os
import sys
'''
customer is going to have two functions.
ability to deposit and withdraw

name, amount
'''

class Customer():

    def __init__(self,name,amount):
        self.name=name 
        self.amount=amount

    def withdraw(self,amount):
        
        if amount>self.amount:
            #print(sys.version_info)
            print(f'Error, You are too poor, you only have ${self.amount}')
        else:
            self.amount-=amount
        return self.amount

    def deposit(self, amount):
        self.amount+=amount
        return self.amount

    def showbalance(self):
        print(f"${'{:<10}'.format(self.amount)}")

class Trader(Customer):
    def __init__(self,name,amount):
        super().__init__(name,amount)
        


c = Customer('Richard', 1000000)
c.showbalance()
c.deposit(1000)
c.showbalance()
c.withdraw(2000000)
c.showbalance()