class Parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    #instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

class Bird:
    def __init__(self):
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')

    def swim(self):
        print('swim faster')

#child class
class Penguin(Bird):
    def __init__(self):
        #calls the super() function
        super().__init__()
        print('Penguin is ready')

    def whoisThis(self):
        print('Penguin')

    def run(self):
        print('Run faster')

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


#instantiate the Parrot class
bird1= Parrot("Blu",10)
bird2= Parrot("Woo",14)

#access the class attributes
print("Blu is a {}".format(bird1.__class__.species))
print("Woo is also a {}".format(bird2.__class__.species))

#access the instance attribute
print("{} is {} years old".format(bird1.name, bird1.age))
print("{} is {} years old".format(bird2.name, bird2.age))

if __name__ == '__main__':
    print(bird1.sing("Happy"))
    gren = Parrot("Gren",4)
    print(gren.dance())
else:
    print("something else is happening")
