Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a**b)
16
print(a//b)
0
print(a%b)
2
#assignment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
8
a-=b
a
3
a*=4
a
12
a//=6
a
2
a/=3
a
0.6666666666666666
a%=2
a
0.6666666666666666
b+=1
b
6
b-=2
b
4
b*=5
b
20
b**=4
b
160000
b//=6
b
26666
b%=4
b
2
#comparision operator
a=6
b=8
a.b
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.b
AttributeError: 'int' object has no attribute 'b'
a>b
False
a<b
True
b>a
True
b<a
False
a<=b
True
a>=b
False
a!=b
True
a==b
False
b<=a
False
b>=a
True
a=6
b=6
a==b
True
#logical operator
a=4
b=8
a<b and b>a
True
a<=b and b>=a
True
a!=b 0r a==b
SyntaxError: invalid decimal literal
a!=b or a==b
True
not True
False
not False
True
#dentifyopertor
#dentifyopertor
# identify operator
a=6
type(a)
<class 'int'>
type is int
False
type(a) is int
True
type(a) is not int
False
b=6.7
type(b) is float
True
type(b)is not float
False
c='harry'
type(c) is str
True
type(c) is not str
False
>>>  d=9+7j
...  
SyntaxError: unexpected indent
>>> d=9+7j
>>> type(d) is complex
True
>>> type(d) is not complex
False
>>> e=True
>>> type(e)is bool
True
>>> type(e) is not bool
False
>>> # membership operator
>>> a=1,2,3,4,5,6,7,8
>>> 5 in a
True
>>> 54 ina
SyntaxError: invalid syntax
>>> 64 in a
False
>>> "hurrey " in a
False
>>> 8 is not in a
SyntaxError: invalid syntax
>>> 9 is not in a
SyntaxError: invalid syntax
>>> #bitwise operator
>>> a=4
>>> b=6
>>> a&b
4
>>> bin(4)
'0b100'
>>> bin(6)
'0b110'
>>> aa=7
>>> a=7
>>> b=6
>>> a/b
1.1666666666666667
