# Volume of circle

from math import pi

def volume_of_circle(radius, pi):
    return 4 / 3 * pi * radius ** 3

r = int(input('Enter the radius : '))
result = volume_of_circle(r,pi)

print(result)



'''

# lohit's answer

def area(radius):
    return 3.142 * radius * radius

def volume(area, length):
    print(area*length)


radius = int(input('Enter the radius :'))
length = int(input('Enter the length :'))

volume(area(radius), length)

'''