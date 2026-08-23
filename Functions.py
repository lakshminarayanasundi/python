#Function
#a function is ablock of organized,reusable code and that is used to perform a single or multiple task
#python gives in built func like print,you can make your own func also and this all user define functions.
#function block begin with keyword def followed by the func name and paranthesis(()).

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

  
'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''


'''a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#function
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#**,%,//

'''def calculate(a,b):
    print("the pow is",a**b)
    print("the mod is",a%b)
    print("the intdiv is",a//b)
calculate(10,20)
calculate(4,6)
calculate(30,20)'''


'''def add(a,b):
    print(a+b)
add(5,7)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
        add()
add()'''



#difference between print and return
#print just shows the human user output in the console
#return is a keyword and return is used to terminate the function and gives back a value from the function
'''def mul(a,b):
    print(a*b)
mul(4,5)'''


'''def mul(a,b):
    return a*b
print(mul(4,6))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(2,3)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,6))'''

#task
'''while True:
    def cal():
        a=int(input("a value"))
        b=int(input("b value"))
        option=int(input(choose the option
                                1.add
                                2.sub
                                3.mul))
        if option==1:
           print("add",a+b)  
        elif option==2:
             print("sub",a-b)
        elif option==3:
             print("mul",a*b)
        else:
            print("invalid option")
    cal()'''

#task
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:                            
        a=int(input("a value"))
        b=int(input("b value"))
        option=int(input(choose the option
                            1. add
                            2. sub
                            3. mul))
        if option==1:
            add()
        elif option==2:
            sub()
        elif option==3:
            mul()'''
