def cakes(dictionary):
    for key, value in dictionary.items():
        print(f'cake taste is {key}, price is {value} Rs')



cakes_menu = {}

while True:
    cake_taste = input('Enter the cake taste :')
    cake_price = input('Enter the cake price :')

    cakes_menu[cake_taste] = cake_price

    another = input('Enter the another cakes (y/n) :')

    if another == 'y':
        continue
    else:
        break

cakes(cakes_menu)