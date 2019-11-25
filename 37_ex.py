# using the print statment

# 横並び ,
num = 1

while num <= 10:
    print(num, end=',')
    num+=1


print('\n','---------------------')



# 横並び スペースの場合


num = 1

while num <= 10:
    print(num, end=' ')
    num+=1

print('\n','---------------------')



#  square number = 平方数,自乗(a*a)

# 自分で書いたコード
# count = 1
# num = 1
# user_num = int(input('Enter the number :'))
# while count <= user_num:
#     print(num*num)
#     num += 1
#     count += 1

# n = int(input('Enter the number :'))
# a = 1

# while a <= n:
#     print(a*a)
#     a += 1



print('\n','---------------------')

# 横並び 奇数

num = 1

while num <= 10:
    if num % 2 == 0:
        print(num, end=',')
    num+=1


print('\n','---------------------')

# 横並び 奇数

num = 1

while num <= 10:
    if num % 2 == 1:
        print(num, end=',')
    num+=1



'''
# 偶数、奇数の答え
# i = 0 or i = 1 で奇数か偶数になる

i = 1

while (i<100):
    print(i)
    i+=2



# 奇数と偶数を交互に出す

i = 0

while (i<100):
    print('奇数です',i) or print('偶数です',i+1)
    i+=2





'''








'''
number is 00

a = 1
while a < 10:
    print('number is ',a)
    a+=1
else:
    print('done')

'''