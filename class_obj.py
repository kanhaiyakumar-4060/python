class A:
    count = 0 #Class Attribute   -->classname.attribute
    def __init__(self):
        self.name = "Anmol"      #instance Attribute
    def fun1(self):               #instance Method
        return self.name
    @staticmethod
    def fun2():
        print("Bhak MAdarchod")    #Class Method -->classname.methodname


print(A.count)
obj = A()
print(obj.name)
A.fun2()    #error
print(obj.fun1())

