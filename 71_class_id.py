#printing the content(value) from class based variable

class Enployee:
    #class based ver 
    id='xyz800'
    name='John Com'

    def display(self):
        print('Enloyee Id is ',self.id,'Enloyee name',self.name)

emp=Enployee()
emp.display()