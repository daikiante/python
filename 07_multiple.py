# python program showing how to have multiple inputs using split


# taking all input at once

# x,y = input('Enter the values for x and y :').split()

# print('Value for x :',x)
# print('Value for y :',y)



# a,b,c = input('Enter the values for a , b and c :').split()

# print('Value for a :',a)
# print('Value for b :',b)
# print('Value for c :',c)



# 7と8の総まとめ
# a,b = input('Enter the value for a,b :').split()
# print(f'the value of a {a} and value for b is {b}')
# print('the value of a {0} and value for b is {1}'.format(a,b))

a,b = input('Enter the value for a,b :').split()
a = float(a)
b = float(b)

print(f'the value of a {a:.2f} and value for b is {b:.3f}')