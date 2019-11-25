# functions with return

def sum_of_2(a, b):
    return a + b

x = sum_of_2(10, 20)
print(x)

print('-----------')










'''
returnは値を返して関数を抜ける（終了する）ためのもの
printはコンソールに出力する為のもの
'''



def mul(a,b,c):
    print(a*b*c)

x = mul(1,2,3)
print(x)


print('-----------')


def mul(a,b,c):
    return(a*b*c)

x = mul(1,2,3)
print(x)