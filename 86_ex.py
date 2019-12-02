# sets 
# no dublicate/repeated values

# create an output set which contains only the even numbers that are present in the input list.

input_list = [1,2,3,4,3,3,6,8,9,7,6,54,325,8,8,978,425,32,5,68,87,3]

output_set = set()

for var in input_list:
    if var %2 == 0:
        output_set.add(var)

print('output set', output_set)

print('------------------------')


input_list = [1,2,3,4,5,6,7,8,9,10]

set_using_comp = {var for var in input_list if var %2 == 0}

print('Output Set using set comprehensions',set_using_comp)

# list => []
# tuple => ()
# dict => {}
# set => {}