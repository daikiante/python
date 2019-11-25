# for loop with format methods

boxes = ['lohit','rohit','ken','masa','miwa','kojun']

for box in boxes[0:4]:
    if box == 'ken':
        print(f'{box}--------hey man...','konnichiwa',box)

    # else:
    #     print(f'hello to all my friend')

print('-------------------------------------------')






# 縦に出力される
# for val in 'lohit is waiting for daiki song':
#     print(val):


for val in 'lohit is waiting for daiki song':
    if val == 'l':
        print('this is l')

    else:
        print(val)