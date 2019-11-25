# dict syntax
# dict = {'index':'value'}

num = {'words':'lohit','num':35,'school':'spiceup'}

for k in num:
    print(k)

print('------------------------------------------')


for v in num.values():
    print(v)


print('------------------------------------------')

i,j = (1,2)
print(i,j)

print('------------------------------------------')

for i,j in [(1,2),(3,4),(5,6)]:
    print(i,j)


print('------------------------------------------')

# it will be tuple
for v in num.items():
    print(v)


# .items()  =  ひとつづつ取り出せる
d = {'name':'lohit','age':20,'school':'spiceup'}

for k,v in d.items():
    print('key =',k,'value =',v)