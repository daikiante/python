# tuple data types
# tuple I cant change value later

a=100,'lohit'
print(a)

list=(1,2,3,4,'lohit')
print(list)

# select by index
print(list[0])
print(list[1])
print(list[2])


tup='python','program'
print(tup)

# adding 2 tuple2s
# concat

tuple1 = (100,200,300)
tuple2 = ('lohit','python')
tuple3 = tuple1 + tuple2
print(tuple3)



# length of tuple 中に入ってるアイテムをカウントしてくれる

tuple10=('python','php','java','rails')
print(len(tuple10))

tuples=('abc',387384,567.890,'john','php')
tinytuple=(123,'jkl')

print(tuples[2:])
print(tuples[0:3])
print(tuples[:])
print(tinytuple*3)
# print concatenated lists
print(tuple10 + tinytuple)

# 逆から表示
print(tuples[::-1])


# tup=('physics','maths',1090,249)
# print(tup)
# del tup
# print(tup)


# nested tuples
n_tuple = ('mouse trap',[1,2,3,4,5],(9,8,7,6,5,'lohit'))

print(n_tuple)
print('--------------------------')


print(n_tuple[1])
print('--------------------------')

# グループの中を指定できる
print(n_tuple[1][1])
print('--------------------------')

# グループの中の中まで指定できる
print(n_tuple[2][5][3])


# ステップとマイナスの概念
my_tuple = ('p','r','o','g','r','m','i','z')
print(my_tuple[:-5])
print('--------------------------')

print(my_tuple[0:5])
print(my_tuple[0:5:2])

# マイナスは右から数える
print(my_tuple[0:-2])


# in operater

my_new_tuple = ('a','b','c','d','e')
print('a' in my_new_tuple)
print('sei' in my_new_tuple)

# not-in operater
print('sei' not in my_new_tuple)


tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"
print(tuplex)
#tuples are immutable, so you can not remove elements
#using merge of tuples with the + operator you can remove an item and it will create a new tuple
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
#converting the tuple to list
listx = list(tuplex) 
#use different ways to remove an item of the list
listx.remove("c") 
#converting the tuple to list
tuplex = tuple(listx)
print(tuplex)
# 折りたたむ
