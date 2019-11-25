# area of circle

def area_of_circle(radius,pi=3.14):
    return radius ** 2 * pi

r = int(input('How long radius? :'))

x = area_of_circle(r)

print(x)




print('---------------')


# area of triangle

def area_of_triangle(base,height):
    return base * height / 2

b = int(input('How long base? :'))
h = int(input('How long height? :'))

x = area_of_triangle(b,h)

print(x)


print('---------------')

# 4!

def fact(x):
    if x == 0:
        return 1
    
    return x*fact(x-1)

x = int(input('Enter the values for x :'))
print(fact(x))

