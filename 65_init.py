class Person:
    def __init__(ok, name, id, school,):
        ok.name = name
        ok.id = id
        ok.school = school

    def myFunction(good):
        print(f'hello my school name is {good.name}.my id is {good.id} Im graduate at {good.school}')

    def myFunction_1(good):
        print(f'hello my school name is {good.name}.my id is {good.id} Im graduate at {good.school}')

create_instance = Person('KLETECH','290','september')
create_instance.myFunction()

print('-------------------------------------')

create_instance_1 = Person('Spiceup','1214','December')
create_instance_1.myFunction_1()