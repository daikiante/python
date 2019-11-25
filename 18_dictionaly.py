# # 混乱するので基本的には{}だけ使う

store = {'name':'lohit','age':20,'job':'spiceup'}

print(store)

print(store['job'])

print('--------------------------------------------')



# empty dictionaries

store = {}
print(store)

# assinging the value to the dictionary potision

store['name'] = 'Yuri'
print(store)

store['age'] = 21
store['phone'] = 8934751947
store['job'] = 'manager'

print(store['phone'])

print('--------------------------------------------')


tinydict = {'name':'lohit','number':974587342,'country':'India'}

print(tinydict)

print(tinydict.keys())

print(tinydict.values())
print('--------------------------------------------')


# using dictionary (important)

d = {0:10,1:20}
print(d)
d.update({2:30})
print(d)

# White a Python script to merge two Python dictionaries.

d1 = {'a':100,'b':200}
d2 = {'x':300,'y':400}
d = d1.copy()
d.update(d2)
print(d)

# Creating an empty Dictionary
Dict = {}
print('Empty Dictionary: ')
print(Dict)

# Creating a Dictionary
# with Integer Keys
Dict = {1:'Geeks', 2: 'For', 3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary  
# with Mixed keys 
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 