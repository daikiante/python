# functions with some input values

def spiceup(owners,staffs):
    print('hello to the world of spiceup', owners, 'and welcome to', staffs)

own = input('Enter the name of the owner :')
stf = input('Enter the name of staff :')

spiceup(own,stf)

print('------------------------')


def total(vegetable,fruit):
    print(f'I bought {vegetable} and {fruit}')

veg = input('what are you bought veg? :')
fru = input('what are you bought fruit? :')

total(veg,fru)