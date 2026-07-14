Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(4,6.7,"python",8+9j,True,False)
print(a)
(4, 6.7, 'python', (8+9j), True, False)
type(a)
<class 'tuple'>
a.index(8+9j)
3
len(a)
6
a.count(True)
1
#sets{}
a={4,7.8,"pooja",5+9j,True,False}
print(a)
{False, True, (5+9j), 4, 7.8, 'pooja'}
type(a)
<class 'set'>
b={7,9,4,6,7,10,20,3}
print(b)
{3, 4, 20, 6, 7, 9, 10}
#add()
a={4,5,6,7,8,9,15}
a.add(15)
a
{4, 5, 6, 7, 8, 9, 15}
#issubset()
a={3,4,5,6,7,8,9}
b={6,7,8,9}
b.issubset(a)
True
a.issubset(b)
False
a={5,6,7,8,9,10,11}
b={7,8,9,10}
a.issuperset (b)
True
b.issuperset (a)
False
#union()
a={3,4,5,6,7}
b={1,2,3,4,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}
#intersection()
a={3,4,5,6,7}
b={1,2,3,7,8,9}
a.intersection(b)
{3, 7}
b.intersection{a}
SyntaxError: invalid syntax
b.intersection(b)
{1, 2, 3, 7, 8, 9}
#differnce()
a={7,8,9,10,11,12,13}
b={8,9,10,11,12,13,14,15}
a.difference(b)
{7}
b.difference(a)
{14, 15}
#update()
a={2,3,4,5,6}
b={1,4,5,6,7,8,9}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9}


#symmetric_differnce()
a={2,3,4,5,6,7,8}
b={1,4,6,8,9,10,11}
a.symmetric_ difference(b)
SyntaxError: invalid syntax
a.symmetric_difference(b)
{1, 2, 3, 5, 7, 9, 10, 11}


#differnce_update()
a={4,5,6,7,8,9}
b=1,2,3,4,5,6,10}
SyntaxError: unmatched '}'
a.difference_update(b)
a
{5, 7}
b={1,2,3,4,5,6,10}
a.difference_update(b)
a
{7}
a={3,4,5,6,7,8}
b={5,6,7,8,9,10}
a.intersection_update(b)
a
{8, 5, 6, 7}
b.intersection_update(a)
b
{8, 5, 6, 7}
a={11,12,13,14,15,16}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{17, 18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 11, 12, 13, 14, 15}

#pop()
a={3,4,5,6,7,8}
a.pop()
3
a
{4, 5, 6, 7, 8}
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
>>> a.remove(6)
>>> a
{4, 5, 7, 8}
>>> #copy
>>> #copy
>>> a={10,20,30,40,50}
>>> a.copy()
{50, 20, 40, 10, 30}
>>> b=a.copy()
>>> b
{50, 20, 40, 10, 30}
>>> a.discard(50)
>>> a
{20, 40, 10, 30}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(100)
>>> b
{100}
>>> 
>>> 
>>> #disjoint()
>>> a={2,3,4,5,6}
>>> b={6,7,8,9,10}
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> c={10,20,30,40}
>>> d={50,60,70,80}
>>> c.isdisjoint(d)
True
