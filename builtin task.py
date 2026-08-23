#print(),input(),max(),min(),
'''a=1
b=2
print(a+b)

#input()
a=input("enter the name")
print(a)'''

#max()

#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))'''


#print(dict(a))
'''b=dict.fromkeys(a)
print(a)
c=dict.fromkeys(a,"pooja")
print(c)

c["o"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''


'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple connection into one connection.
'''a=[10,20,30,40,50,60]
names=["sowmya","priya","kanya","preethi","harika"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)

d=list(zip(a,names))
print(d)


d=list(zip(a,names))
print(*d)'''

#enumerate()->we can give counter to the collection
'''names=["hemanth","vasu","roop","sai","spider"]
for i in range(len(names)):
    print(i,names[i])


b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)'''


#railway ticket
while True:
    def railway_ticket():
        ticket=1000
        gender=input("enter the gender")
        age=int(input("enter the age"))
        if gender=="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                print(ticket)
        elif gender=="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age<60:
                print("normal citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
    railway_ticket()                   


