'''
Create a Vending machine that will take money and store items
'''


class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            # raise exception for missing item
            pass
        self.stock -=1

class VendingMachine:
    def __init__(self):
        self.bank = 0
        self.items = []
        self.headers = ['Item','Price','Qty']

    def addItem(self, item):
        self.items.append(item)

    def showItems(self):
        print(self.headers)
        for item in self.items:
            print(item.name, item.price, item.stock)

    def addCash(self, money):
        self.bank += money
    
    def showCash(self):
        print(f'Currently you have: {self.bank} tokens')

    def buyItem(self , itemWanted):
        
        for item in self.items:
            if item.name == itemWanted:
                break
            print('Item Not available')

        else:
            self.bank -= item.price
            item.buyFromStock()
            print('You got ' +item.name)
            print('Cash remaining: ' + str(self.amount))

newvending=VendingMachine()
item1 = Item('Vegan Eggs' , 10.00, 1)
newvending.addItem(item1)