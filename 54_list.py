def person(dictionary):
    belts = list(dictionary.values())

    for belt in belts:
        num = belt.count(belt)
        print(f'There are {num} {belt} belts')





lohit_items = {}

while True:
    lohit_belt = input('Enter the name of belt :')
    lohit_belt_color = input('Enter the color of belt :')

    lohit_items[lohit_belt] = lohit_belt_color
    another = input('Enter another item (y/n) :')

    if another == 'y':
        continue
    else:
        break

person(lohit_items)