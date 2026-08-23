#oops
#syntax
'''class classname():
    #attributes
     name="pooja"
     age=28
     place="vja"
     def fname(method_name):
         print("statements...............")
a=classname()
print(dir(a))
a.fname()'''

#class declaration
''''class Details():
    name="Lucky"
    age=22
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''


#object instantiation
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("Lucky",22,"vja")
a.display()   
b=Details()
b.data("Hemanth",22,"ten")
b.display()'''


#object initialization
'''class Data():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Data("Lucky",22,"vja")
print(dir(a))
a.display()'''


'''class Data():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
            print(self.name,self.age,self.place)
a=Data()
print(dir(a))
a.display()'''

'''class Data():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
            print(self.name,self.age,self.place)
a=Data(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()'''

#diff b/w _ and _
'''class Employee() :
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@codegnan.com"
        self.__salary=10000#private variable
class Employee1() :
     def __init__(self):
         self.name="lucky"
         self._mailid="lucky@codegnan.com"
         self.__salary=1000000
a=Employee()
b=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(dir(b))
print(b.name)
print(b._mailid)
#print(a.__salary)
print(a._Employee__salary)
print(b._Employee1__salary)'''

#polymorphism
#operator overloading
'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(6))
print(a.__pow__(2))
#print(a.__div__(4))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(10))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b).title())'''

#operator overriding
'''class A() :
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B() :
    def __init__(self,b):
        self.b=b
x=A(6)
y=B(4)
#x=6
#y=4
print(x+y)'''

'''#method overloading
class new() :
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("program ends....")
a=new()
#a.sum()
#a.sum(3,6,8)
a.sum(4,5)'''


#method overriding
'''class Animal() :
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog can barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''
        
    
      

