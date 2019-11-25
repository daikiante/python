# functions with the default values

def greet(name='lohit',age=20,country='India',work='spiceup'):
    print(f'my name is {name}, my age is {age}, from {country}, I working {work}')

greet()

greet('daiki',23,'Japan','student')



print('--------------------------------')




def calls(name='lohit'):
    print(name)

calls(name='sei')



print('--------------------------------')


def get_sum(num_1=5,num_2=10):
    print(num_1 * num_2)

num_1 = input('Enter num 1 :')
num_2 = input('Enter num 2 :')