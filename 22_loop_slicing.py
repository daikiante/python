# slicing in for loop

offices = ['lohit',12345,'sei','daiki',90989,'python','KLE']

# want only =====> 'lohit',12345,'sei'

for office in offices[0:3]:
    print(office)

# check the item is matching

for office in offices:
    if office == 'python':
        print('the programming language is',office)
        break
    
    elif office == 'KLE':
        print('the university is',office)

    else:
        print('all other is',office)
        