# calculating with *args

def calculate(*args):
    print(sum(args))

calculate(10,20,40)

print(calculate)


print('------------')

def calculate(*args):
    sum = 0
    for arg in args:
        sum = sum + arg
    print('the sum is',sum)

calculate(10,20,30,40)