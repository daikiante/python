
def names(dictionary):
    for key, value in dictionary.items():
        print(f'At spiceup {key} is handled by {value}')




assignment = {}

while True:
    program = input('Enter the name of programming langage :')
    student = input('Enter the student name :')
    assignment[program] = student
    another = input('Do you want to add one more item (y/n) :')

    if another == 'y':
        continue

    else:
        break


names(assignment)