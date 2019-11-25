# 5!

number = int(input('Enter number:'))

fac = 1

for i in range(1,number + 1):
    fac = fac * i

print(number,'! is',fac)