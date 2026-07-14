Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len()
a="codegnan"
len(a)
8
b="python course"
len(b)
13
c=" "
len(c)
1
d=""
len(d)
0
e="i am in vja"
len(e)
11
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="python"
a[1]
'y'
a.find("h")
3
b="hello"
b.find("1")
-1
b.find("h")
0
#escape sequences
#\n->new line
#\t->tab space
a="name\nmailid\tmobileno\nncollege\tbranch"
a
'name\nmailid\tmobileno\nncollege\tbranch'
print(a)
name
mailid	mobileno
ncollege	branch
b="name:lakshmi narayana\nmailid:lakshminarayana@gmail.com\ntmobileno:6309355662\ncollege:sietk\tbranch:cse"
print(b)
name:lakshmi narayana
mailid:lakshminarayana@gmail.com
tmobileno:6309355662
college:sietk	branch:cse
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("p","c")
'cython java'
c="wait wait until you succeed"
c.replace("wait","work")
'work work until you succeed'
c.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="code"
a.upper()
'CODE'
#lower
#lower
b="HELLO"
b.lower()
'hello'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.tittle()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
e=" i am in class"
e.capitalize()
' i am in class'
a="code"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="code course"
b.isalpha()
False
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
a="pooja1234"
a.isalnum()
True
b="pooja.@1234"
b.isalnum()
False
c="pooja.1234"
c.isalnum()
False
a="data science"
a.startswith("d")
True
a.endswith("e")
True
#strip()
#lstip(),rstrip()
a="    pooja    "
a.strip()
'pooja'
a.lstrip()
'pooja    '
a.rstrip()
'    pooja'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i love python"
b.split()
['i', 'love', 'python']
b="html","css","js","bs"
#join()
"".join(b)
'htmlcssjsbs'
" ".join(b)
'html css js bs'
"k".join(b)
'htmlkcsskjskbs'
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname+" "+lname)
pooja ch
print(fname.tittle()+" "+lname.tittle())
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    print(fname.tittle()+" "+lname.tittle())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
>>> print(fname.title()+" "+lname.title())
Pooja Ch
>>> #formatting
>>> a=5
>>> b=7
>>> print(a+b)
12
>>> print("the sum is",a+b)
the sum is 12
>>> city="vja"
>>> print("city is",city)
city is vja
>>> #format()
>>> a="motu"
>>> b="pathlu"
>>> print("hello {}{}".format(a,b))
hello motupathlu
>>> print("hello {} {}".format(a,b))
hello motu pathlu
>>> print("hello {}hello {}".format(a,b))
hello motuhello pathlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathlu
>>> print("hello {} \n hello {}".format(a,b))
hello motu 
 hello pathlu
>>> #fstring
...  
>>> a="sitha"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitharam
>>> print(f"hello {a} {b}")
hello sitha ram
>>> print(f"hello {a} hello {b}")
hello sitha hello ram
>>> print(f"hello {a}\nhello {b}")
hello sitha
hello ram
