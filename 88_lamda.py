# why use Lamda functions?
# The power of lamda is better shown when you use them as an anoymous/unknown function inside another function.

# Say you have  a function definition that takes one argument, and that argument will be multiplied with an unknown number

x = lambda a:10+a

print(x(2))


# equation
# y = 20 + b

y = lambda b:20+b
print(y(10))










# equation = Y**X

'''
x = int(input('Enter the number :'))
y = int(input('Enter the number :'))

total = y**x

print(total)
'''

# ↑これをラムダで書くと...

equ = lambda x, y: y**x
print(equ(2,3))


# EX

equ = lambda x, y, z: x + y + z
print(equ(1,2,3))



# lambda in function
# myfunの3はn rの11はa に代入されている

def myfun(n):
    return lambda a:a*n

r = myfun(3)
print(r(11))