#super()
'''class parent():#super class
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("pooja",28)
print(a.age)
print(a.name)'''
#encapusuluation
#combining multiple units into single unit is called a encapsulation.
#public data,private data,protected data.
#publicdata
'''class A():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
obj1=B()
obj1.method1()
obj1.method2()'''

#_proteteddata
'''class A():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
obj1=B()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''

#__privatedata
'''class A():
    __privatedata="pooja"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
obj1=B()
obj1.method1()
obj1.method2()'''

 
    
