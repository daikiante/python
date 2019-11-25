# Format method in if-condition

num = int(input('Enter number :'))

if (num%2) == 0:
    print('{0} is a even number'.format(num))

else:
    print('{0} is a odd number'.format(num))



food = input('do you eat meat :')

if food == 'yes':
    print('he is non-veg')

else:
    print('veg man')