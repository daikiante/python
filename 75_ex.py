# we have a class defined variable

# Exercise
# We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Junm worth $10,000.00

class Vehicles:

    def __init__(self,name, cost, color):
        self.name = name
        self.cost = cost
        self.color = color

    def discription(self):
        print(f'{self.name} color is {self.color},and cost is ${self.cost}')


car1 = Vehicles('Fer','60,000.00','red')
car1.discription()

car2 = Vehicles('Junm','10,000.00','blue')
car2.discription()

