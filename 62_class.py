'''

create a class named Gender, Use the __init__() function to assign values for name and age etc

'''
# init => initialize / started

class Gender():
    
    def __init__(self, name, age, program, health):
        self.name = name
        self. age = age
        self. program = program
        self. heal = health

variables = Gender('sei', '25', 'python', 'so-so')

print(variables.name)


print('-----------------------------------------------')


class Teeth():

    def __init__(self, pain, doctor):
        self.pain = pain
        self.doctor = doctor

instance = Teeth('hard',"don't wanna go")
print(instance.pain)
print(instance.doctor)