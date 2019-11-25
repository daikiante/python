'''

In the below program, if your input is 0, while loop will "break" and the code
inside "else" clause will not get executed.
If you are using other numbers as input, while loop will complete its full cycle
and the code inside "else" clause will be considered

breakには"ループを抜ける"性質がある。
breakが先に適用された場合、elseは適用されない。


'''



# While with "else"

# a = 1

while a <= 3:
    b = int(input('Enter the number :'))
    if b == 0:
        print("exiting loop with break command, 'else' is not executed")
        break
    a += 1
else:
    print('loop exited with out executing break command')


