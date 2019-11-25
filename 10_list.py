'''
                    [List]
list vlues can be changed later,  we will them as mutable
I can store different type of data types

( )  tuple
[ ]  list

'''

words = [1,2,3,4,5,6,'lohit','yuri',True,12.34,('lohit','john')]

print('my list is',words)

print(words[6])
print('---------------------------')

print('lohit' in words)

words[6] = 'daiki and sei'

print(words[6])

print('---------------------------')
print(words[10][0])


print('---------------------------')
print('lohit' in words)

print('---------------------------')

print(('lohit','john') in words)

print('-'*20)

# .append

'''
append function in list
it adds the new element at last
'''

create = ['maths','science']
create.append('python')

print(create)

# insert() : Insert an elements at specified potision.

one_more = ['maths','science']
one_more.insert(1,'python')
print(one_more)


# extend in list (can't use tuple)
# extend() : Adds contents to name2 to the end of name.

name = ['lohit','john','daiki','sei']
name2 = [1,2,3,4,5,6,7]

name2.extend(name)
print(name2)


