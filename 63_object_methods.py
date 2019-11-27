# object methods

'''
* objects can also contain methods
* methods are kind of functions
* the functions belongs to the class
'''

class Subject():
    
    def __init__(self, language, greet):
        self.language = language
        self.greet = greet

    def MyDialog(self):
        print('I can speak ', self.language)
        print('I wish you ', self.greet)

    def MyDialog_1(self):
        print('I can speak ', self.language)
        print('I wish you ', self.greet)


instance = Subject('English', 'Good Mornig Guys')
print(instance.language)
instance.MyDialog()

print('------------------------------------')

instance_1 = Subject('Japanese', 'Good Mornig Guys')
print(instance_1.language)
instance_1.MyDialog_1()


