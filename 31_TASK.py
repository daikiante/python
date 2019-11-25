
empty_list = []
user_num = int(input('Enter the number:'))

for x in range(1,user_num +1):
    empty_list.append(x)

print(empty_list)

print(sum(empty_list))

print('-------------------------')

# find the average of list

average = sum(empty_list) / user_num
print(average)