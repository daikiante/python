# functions with some parameters/arguments

def students(name,classes):
    print(f'hello Im {name}, Im new to class of {classes}')
    print('Hello', name, 'what are you doing in this class', classes)

students('lohit','python')


print('-------------------')


def data(age,country):
    born_in = 2019 - int(age)
    print("He's age is", age, 'He from',country)
    print('He was born in',born_in)

data('20','japan')

