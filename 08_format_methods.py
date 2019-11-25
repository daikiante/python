# in this program we will learn how to print variables using {}

# lets some numbers

number1 = 300.1345678
number2 = 2.3456778
number3 = 20.20204023
number4 = 2333.543554


# 1st method
print('Lottory number 1 is {0} and cecond Lottory No is {1}'.format(number1,number2))

# for printing the total 4 digits　大きい位から.○桁を表示
print('Farst number is {0:.4} and cecond number is {1} and third number is {2:.3}'.format(number1,number2,number3))

# fractional points 小数点から下の2桁を表示
print('first number is {0:.2f}'.format(number1))



# 2nd method
print(f'the prize number is {number1} and second number is {number2}')
# ''の前に付くfはフォーマット、.4fに付くのはfractional
print(f'number first {number1:.4f}')