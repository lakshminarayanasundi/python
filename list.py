Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,4,5,"python",6+9j,True,False]
print(a)
[2, 4, 5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
#append
a=["python","c","c++"]
a.append("java")
a
['python', 'c', 'c++', 'java']
a.append("htm","css")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.append("htm","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', ['html', 'css']]
#extend
a=["html","css","js"]
a.extend(["python","java"])
a
['html', 'css', 'js', 'python', 'java']
#insert()
b=["vja","hyd","vzg"]
b.insert(1,"chennai")
b
['vja', 'chennai', 'hyd', 'vzg']
a=["apple","banana","grapes"]
a.index("graps")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.index("graps")
ValueError: list.index(x): x not in list
a.index("grapes")
2
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']
a.count("apple")
1
len(a)
3
d="apple"
len(d)
5
e=["apple"]
len(e)
1
a=["mango","kiwi","dragon","berry"]
a.sort()
a
['berry', 'dragon', 'kiwi', 'mango']
b=[9,3,7,0,20,40,23,78]
b.sort()
b
[0, 3, 7, 9, 20, 23, 40, 78]
#reverse
a=["ds","ai","ml"]
a.reverse()
a
['ml', 'ai', 'ds']
b=[5,7,9,2,0,1]
b.reverse()
b
[1, 0, 2, 9, 7, 5]
#pop
a=["black","white","red","blue","pink"]
a.pop()
'pink'
>>> a
['black', 'white', 'red', 'blue']
>>> a.pop(2)
'red'
>>> a
['black', 'white', 'blue']
>>> a.pop("black")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.pop("black")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove("black")
>>> a
['white', 'blue']
>>> 
>>> 
>>> #clear
>>> a=["ap","ts","ka"]
>>> a.clear()
>>> a
[]
>>> b[]
SyntaxError: invalid syntax
>>> b.append("pooja")
>>> b
[1, 0, 2, 9, 7, 5, 'pooja']
>>> b=[]
>>> b.append("Lucky")
>>> b
['Lucky']
>>> #extend
>>> a=[10,20,30,40,"code"]
>>> a.split()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.split()
AttributeError: 'list' object has no attribute 'split'
>>> a.extend(["code"])
>>> a
[10, 20, 30, 40, 'code', 'code']
