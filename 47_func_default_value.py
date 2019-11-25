# functions with default value

def subjects(name='python', course='Django', time=3):
    print(f'if you take {name} and {course} , you need {time} months of finish')

subjects()
subjects('PHP','laravel',2)

subjects('psyco','neural net')

subjects(4)