#inheritance

class Culation1:
    def Summation(self,a,b):
        return a+b
class Calation2:
    def Multiplicatjion(self,a,b):
        return a*b
class Darived(Culation1,Calation2):
    def Darived(self,a,b):
        return a/b

#
d=Darived()
print(d.Summation(10,20))

print(d.Multiplicatjion(10,20))

print(d.Darived(20,10))