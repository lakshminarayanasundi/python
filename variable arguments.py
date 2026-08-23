#variable length arguments
#variable arguments are automatiacally stores in tuple and we use in star arguments

'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
b=[4,5,6,7,8]
check(*b)
c={6,7,8,9,10}
check(*c)
d={"name":"lucky","city":"vja"}
check(*d)'''


'''def check1(*a):
    d=2#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(1,3,2,5,.2,3.4)
check1(3,4,2,5,3.6,2.4,"pooja")'''



#kwargs(**)

'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''


'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["sai","siva","ravi"],
         "status":["p","a","p"]}
check(**details)'''


#both * and ** usage
'''def final(*a,**b):
    d=3#creating  variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("keys is",i)
        print("value is",j)
final ()
data=(2,3,4,3.5,6.2)
final(*data)
details={"idnos":[10,20,30],
         "names":["pooja","priya","preethi"],
         "status":["p","a","p"]}
final(**details)
final(*data,**details)'''

#max(),min(),sum()
'''print(max(5,7,9,10,20,40))
print(min(4,'''
#marks analysis report
students=int(input("enter the no.of students"))
marks=[]
for i in range(1,students+1):
    mark=int(input(f"enter the student {i} marks"))
    marks.append(mark)
for i in marks:
    print(i)
print(".............marks analysis report................")
print("total students",students)
print("heighest marks",max(marks))
print("lowest marks",min(marks))
print("total marks",sum(marks))
print("average",sum(marks)/students)
    

        
