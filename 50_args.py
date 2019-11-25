# python program to show *args for variable number of arguments
# 複数の引数を受け取る場合、先頭に*をつける。

def home(*argv):
    for arg in argv:
        print(arg)

home('lohit','koramangala','450','2nd floor')


