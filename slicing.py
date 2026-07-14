Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> b= "work until you succeed"
>>> b[0:4]
'work'
>>> b[5:10]
'until'
>>> b[11:14]
'you'
>>> b=[15:22]
SyntaxError: invalid syntax
>>> b[15:22]
'succeed'
>>> c=
SyntaxError: invalid syntax
>>> c="time is precious"
>>> c[8:12]
'prec'
>>> c[8:15]
'preciou'
>>> c[8:16]
'precious'
>>> c[:4]
'time'
>>> a="simple is better than complex"
>>> a[-19:-13]
'better'
>>> a[-29:-23]
'simple'
>>> a[-7:]
'complex'
>>> b="codegnan it solutions"
>>> b[-21:-13]
'codegnan'
>>> b[-9:]
'solutions'
b[-9:-1]
'solution'
#striding
a="data science"
a=[::]
SyntaxError: invalid syntax
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
