year = int(input('Enter the year :'))

if year % 100 == 0:
    print(f'{year} is common year')
elif year % 4 == 0 or year % 400 == 0:
    print(f'{year} is leap year')
else:
    print(f'{year} is common year')
