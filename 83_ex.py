
# squaring the only even numbers in list

numbers = [1,2,3,4,5,6,7,8,9]

square = []

for number in numbers:
    if (number**2)%2 == 0:
        square.append(number**2)
print(square)


# now lets do it comprehension way

square = [number ** 2 for number in numbers if (number ** 2)%2 == 0]

print('_____',square)


print('---------------------')


# Constructing output list using for loop

output = []
for var in range(1, 10):
    output.append((var **2) - 1)
print('the solution would be',output)


print('---------------------')


outputs = [(var **2) - 1 for var in range(1, 10)]

print('output is',outputs)




print('---------------------')

# create a list of only Kisu numbers

number = [1,2,3,4,5,6,7,8,9,10]

add = []

for num in number:
    if (num % 2) == 0:
        add.append(num + 1)
print(add)

# comprehension way

add = [num + 1 for num in number if (num % 2) == 0]
print(add)
