
def printme(*names):
    print('which data type is add', type(names))
    print('printing the passed arguments')

    for name in names:
        print(type(name))

# calling the function
printme(100, 10.09, 'lohit')


