'''def greetings(name):
    print("welcome",name)'''
    
'''a=int(input("enter the  a value"))
b=int(input("enter the b value"))
print("the sum is:",a+b)'''


'''details={"idnos":[10,20,30],
         "names:[charan","prabhas","nani"],
         "marks":[70,80,90]}'''

'''if __name__=="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''


'''def dummy():
    if __name__=="_main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''


#math module
'''import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,4))
print(math.log(2))
print(math.tan(45))
print(math.sin(60))
print(math.cos(30))
print(math.ceil(2.9))
print(math.ceil(5.9))
print(math.ceil(8))
print(math.floor(2.7))'''

'''from math import pi,log,sqrt
print(pi)
print(log(10))
print(sqrt(2))'''

#sys module
'''import sys
print(sys.path)
print(sys.version)'''
#os module
#import os
'''print(os.path)
print(os.getcwd())
print(os.listdir())'''

'''print(os.mkdir("aug4"))
print(os.listdir())'''

'''print(os.chdir("C:\\Users\\USER\\Downloads"))
print(os.listdir())'''

#ASCII
'''print(chr(67))

print(chr(65))

print(chr(90))

print(chr(93))

print(ord("a"))

print(ord("z"))
#print(ord(97))#error
print(chr(97))'''


'''for i in range (65,91):
    print(chr(i),end=" ")


for i in range(97,123):
    print(chr(i),end=" ")'''


a=input("name")
for i in a:
    print(i,"-",ord(i))

