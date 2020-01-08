class Computer:

    def __init__(self):
        #encapulation
        #double __ is private
        #single _ is protected
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


class Parrot:
    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

#common interface
def flying_test(bird):
    bird.fly()

#instantiate object
blu = Parrot()
peggy = Penguin()
#passing the object
flying_test(blu)
flying_test(peggy)



#initialize the variable
c = Computer()
c.sell()

#changing price using variables.
c.__maxprice = 1000
c.sell()

#using setter
c.setMaxPrice(4000)
c.sell()
