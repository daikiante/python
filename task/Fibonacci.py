x = 0
y = 1
r = 0

while y < 10000:
    r = x + y
    print(r)
    x = r + y
    print(x)
    y = x + r
    print(y)


# def fib(n):
#     if n<0:
#         print('Entered value is wrng')
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+ fib(n-2)
# print(fib(9))