# self parameter
'''
the self parameter is reference to the current instance of the class, and is used to access varibles that belongs to the class.

It does not have to be names self, you can call it anything you want to call.

*But it has to be first parameter of any function in the class.
'''

class Subject:
    def __init__(anything, working, salary):
        anything.working = working
        anything.salary = salary

    def myWork(anything):
        print(f'if you work as {anything.working}, you get paid {anything.salary}')

    def myWork_1(anything):
        print(f'if you work as {anything.working}, you get paid {anything.salary}')

create = Subject('Python developer','very good salary')
create.myWork()

print('-------------------------------------')

create_1 = Subject('Spiceup teacher','very high salary')
create_1.myWork()
