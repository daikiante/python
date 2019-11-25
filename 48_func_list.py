# only for the list
def myFun2(x):

    x[0] = 120
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x
    x = [20, 30, 40]

# DriverCode (Note that lst is not modified)
# after function call
lst = [10, 11, 12, 13, 14, 15]
myFun2(lst)
print(lst)







# This is not list
def myFun(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x
    x = 20
    print('---value here is 20---')

x = 10
myFun(x)
print(x)