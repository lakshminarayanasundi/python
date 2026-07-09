Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=5
type(a)
<class 'int'>
b=7.8
type(b)
<class 'float'>
c="lucky"
type(c)
<class 'str'>
x=5+9j
type(x)
<class 'complex'>
y=8+6j
type(y)
<class 'complex'>
c=true
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
c=True
type(c)
<class 'bool'>
f=False
type(f0
     type(f)
     
SyntaxError: '(' was never closed
type(f)
     
<class 'bool'>
>>>  #int
...      
>>> int(9)
...      
9
>>> int(hi)
...      
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(hi)
NameError: name 'hi' is not defined
>>> int(6+8j)
...      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
...      
1
>>> int(False)
...      
0
>>> #float
...      
>>> float(True)
...      
1.0
>>> float(False)
...      
0.0
>>> #str
...      
>>> str(True)
...      
'True'
>>> str(9+6j)
...      
'(9+6j)'
>>> #complex
...      
complex(8)
     
(8+0j)
complex(6+3j)
     
(6+3j)
complex(True)
     
(1+0j)
complex(False)
     
0j
#boolean
     
bool(8)
     
True
bool(true)
     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
bool(True)
     
True
bool(False)
     
False
