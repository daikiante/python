# class name:
#     def say(self,name):
#         return name
# class age(name):
#     def talk(self,age):
#         return age
# class address(name):
#     def print_this(self,address):
#         return address
# ok=address()
# print(ok.say('lohit'))

#this will give errorr
#do_it=age()
#print('do_it.say(1000))

# call=age()
# print('my age is',call.talk('100'))

class Father:
    def singer(self,quelity):
        return quelity

class Mather:
    def cook(self,cook):
        return cook

class Son(Father,Mather):
    def artist(self,son_quelity):
        return son_quelity

class GrandSon(Son):
    def turist(self,grang_song_quelity):
        return grang_song_quelity

some_one_talking_to_grang_son=GrandSon()

print(some_one_talking_to_grang_son.singer('singer'))
print(some_one_talking_to_grang_son.cook('cook'))


