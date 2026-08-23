#exception handling
#try->instructions from which we are expecting the exceptions
#expect->exceptions are raised in try block it will be handle by this block
#else->no exceptions(optional)
#finally->always it will display.
 
#exception handling
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exeption is raised")
    else:
        print("no exceptions")
    finally:
        print("programs ends.........")'''


#file handling
#write()
'''a=open("lucky.txt","w")
b=a.write("python full stack")
a.close()'''

'''a=open("lucky.txt","w")
b=a.write("codegnan it solutions")
a.close()'''

#append
'''a=open("lucky.txt","a")
b=a.write("\tlucky")
a.close()'''

'''a=open("lucky.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("lucky.txt","w")
b=input("data")
a.write(b)
a.close()'''


#readlines()
'''a=open("lucky.txt")
#print(a.read())#it will display the entire content
#print(a.readline())#it will display the first line.
#print(a.readlines())#it will display in list with \n
#print(a.read(9))#it will display no of characters'''

#writelines()->it makes every object side by side
'''a=open("priya.txt","w")
b=["sandeep","sai","vasu","roop","srinadh"]
a.writelines("\n".join(b))#it will word by word \n join(b)
a.close()'''

'''a=open("task 1.py")
print(a.read())'''

'''a=open("C:\\Users\\USER\\OneDrive\\Documents\\compiler")
print(a.read())'''


