# x = False
# y = False

# print('x and is ',x or y)

# 偶数(even number)奇数(odd number)チェック

# number = int(input('Enter the number :'))

# if number % 2 == 0:
#     print('Number is even')

# elif number == 0:
#     print('number is zero')

# else:
#     print('number is odd')



# name = 'rekha'

# if name == 'lohit':
#     print('he is python student')

# elif name == 'chihiro':
#     print('not student she working for management')

# else:
#     print('wrong name')


ticket = int(input('Enter the seat number please :'))

if ticket >= 80 and ticket <= 100:
    print('Welcome to First Class')

elif ticket >= 60 and ticket <= 79:
    print('Business Class')

elif ticket >= 40 and ticket <= 59:
    print('3rd Class')

elif ticket >= 36 and ticket <= 39:
    print('4th Class')

elif ticket >= 100 or ticket <= 0:
    print('not found')

else:
    print('not booked')







