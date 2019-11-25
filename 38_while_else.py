# while or

i = 0

while (i<100):
    print('奇数です',i) or print('偶数です',i+1)
    i+=2


# other way

multiple = 1
i = 2
while multiple <= 100 and i <= 100:
    print(multiple*i)
    i+=2