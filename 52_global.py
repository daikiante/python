# global

'''

def関数の中(local)ではglobal変数は使えない。
global変数を使う場合はlocalの中でglobal変数宣言をして使う。

'''


name = 'lohit'
age = 20

def person():
    global age
    print('my age is',age)

    per = 'lohit badiger'
    print('my name is',per)

person()

print('global name are',name)
print('global age is',age)




# Exsample

num1 = 10
num2 = 3000

def sum():
    global num1
    print(num1 + num2)

sum()
print(num1 + num2)