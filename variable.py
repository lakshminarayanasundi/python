Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=6
>>> print(a)
6
>>> del a
>>> print (a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print (a)
NameError: name 'a' is not defined
>>> 
>>> fname="pooja"
>>> lname="ch"
>>> print(fname+lname)
poojach
>>> print(fname+ lname)
poojach
>>> print(fname+" "=lname)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(fname+" "+lname)
pooja ch
>>> 
...   
>>> name="pooja"
>>> print(name)
pooja
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> print(NAME)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(NAME)
NameError: name 'NAME' is not defined
>>> NAME="POOJA"
>>> print(NAME)
POOJA
