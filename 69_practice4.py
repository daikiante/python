# class myname:
# class based variale
# name='lohit'

# print(myname)

class Good:
    def __init__(self,dress,bad):
        self.dress=dress
        self.bad=bad

    def myFunc(self):
        x=10
        y=20
        print('hello my name is ',self.dress,self.bad)
        print(x+y)
        #もしここに追加したら一緒にプリントされる
sei=Good('new dress ','Im wearing')
sei.myFunc()

