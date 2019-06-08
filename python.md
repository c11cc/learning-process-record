* install python 
```
./configure
make
make install
```
* environment<br>
`export PATH="$PATH:/usr/local/bin/python"`

* install pythonwin<br> 
` pip install pywin32 `
* with source<br>
`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pywin32`

* upgrade pip<br>
` python -m pip install --upgrade.pip `

* start coding <br>
`#_*_coding:utf-8 _*_`
* or<br>
`#_*_coding:unicode _*_`

* note<br>
`start with #, or ''' for multilines.`

### string <br>
`\: escape character `
* r/R:<br>
```
>>>print("this is the first line with\n")
this is the first line with
>>>print(r"this is the second line with\n")
this is the second line with\n
```


### number<br>
```
>>>a,b,c,d=1,1.1,true,1+1j
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b,c,d=1,1.1,true,1+1j
NameError: name 'true' is not defined
>>>a,b,c,d=1,1.1,True,1+1j
>>>print(type(a,b,c,d))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(type(a,b,c,d))
TypeError: type() takes 1 or 3 arguments
>>>print(type(a),type(b),type(c),type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
```

### string<br>
```
>>>e,f="hello",'hello'
>>>e,f
('hello','hello')
>>>len(f)
5
>>> type(f)
<class 'str'>
```

### list<br>
```
>>> a=["I","like",'that','boy','\n']
>>> a
['I', 'like', 'that', 'boy', '\n']
>>> type(a)
<type 'list'>
>>> print(a)
['I', 'like', 'that', 'boy', '\n']
>>> a +['very much']
['I', 'like', 'that', 'boy', '\n', 'very much']
>>> a[4]=[] #list can be edited
>>> a
['I', 'like', 'that', 'boy', []]
>>> a[4]=''
>>> a
['I', 'like', 'that', 'boy', '']
>>> a=["I","like",'that','boy','\n']
>>> a.remove("\n")
>>> a
['I', 'like', 'that', 'boy']
>>> a.append("very much")
>>> a
['I', 'like', 'that', 'boy', 'very much']
>>> a.extend("very muach")
>>> a
['I', 'like', 'that', 'boy', 'very much', 'v', 'e', 'r', 'y', ' ', 'm', 'u', 'a', 'c', 'h']
>>> a.pop(len(a)-1)
'h'
>>>del a[5:len(a)]
>>> a
['I', 'like', 'that', 'boy', 'very much']
>>> b=a[1:5]
>>> b
['like', 'that', 'boy', 'very much']
>>> b.reverse()
>>> b
['very much', 'boy', 'that', 'like']
>>> b.append('I')
>>> b
['very much', 'boy', 'that', 'like', 'I']
>>> b.reverse()
>>> b
['I', 'like', 'that', 'boy', 'very much']
>>> b.sort()
>>> b
['I', 'boy', 'like', 'that', 'very much']
>>> b.copy()
['I', 'boy', 'like', 'that', 'very much']
>>> b[:]
['I', 'boy', 'like', 'that', 'very much']
>>> b.clear()
>>> b
[]
```

### Tuple
```
>>> b=("i",'like','that','boy','\n')
>>> b
('i', 'like', 'that', 'boy', '\n')
>>> b[4]
'\n'
>>> print(b,type(b),len(b))
('i', 'like', 'that', 'boy', '\n') <class 'tuple'> 5
>>> b[4]=() #Tuple cannot be edited
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b[4]=()
TypeError: 'tuple' object does not support item assignment
>>> b[4]=[]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b[4]=[]
TypeError: 'tuple' object does not support item assignment
>>> c=('one')
>>> print(b+c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(b+c)
TypeError: can only concatenate tuple (not "str") to tuple
>>> b=('one','boy')
>>> c=('one','man')
>>> b+c
('one', 'boy', 'one', 'man')
>>> bb=('becomes',)
>>> b+bb
('one', 'boy', 'becomes')
>>> b+bb+c
('one', 'boy', 'becomes', 'one', 'man')
>>> bc=('become')
>>> print(type(bb),type(bc))
<class 'tuple'> <class 'str'>
>>> d,e=('i','have'),('tried','this')
>>> d+e
('i', 'have', 'tried', 'this')
>>> a=['A','B','C']
>>> b=tuple(a)
>>> print(type(a),type(b))
<class 'list'> <class 'tuple'>
>>> a
['A', 'B', 'C']
>>> b
('A', 'B', 'C') 
```


### set,like hash key in perl
```
>>> student={'Tom','Jerry','Fred','Jerry'}
>>> student
{'Fred', 'Tom', 'Jerry'}
>>> 'Tom' in student #like exists in perl
True
>>> teacher=set('ABCD')
>>> teacher
{'A', 'B', 'D', 'C'}
>>> leader=set('CDEF')
>>> teacher-leader
{'A', 'B'}
>>> teacher|leader
{'D', 'F', 'A', 'B', 'E', 'C'}
>>> teacher&leader
{'D', 'C'}
>>> teacher^leader
{'F', 'A', 'B', 'E'}
```

### dictionary, like hash in perl
```
>>> hash={'Tom':'A','Jerry':'B'}# declare method1 
>>> hash
{'Tom': 'A', 'Jerry': 'B'}
>>> hash['Tom']
'A'
>>> hash['Kim']='A'
>>> hash
{'Tom': 'A', 'Jerry': 'B', 'Kim': 'A'}
>>> del hash['Jerry']
>>> hash
{'Tom': 'A', 'Kim': 'A'}
>>> hash.keys()
dict_keys(['Tom', 'Kim'])
>>> hash.values()
dict_values(['A', 'A'])
>>> sorted(hash.keys)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sorted(hash.keys)
TypeError: 'builtin_function_or_method' object is not iterable
>>> sorted(hash.keys())
['Kim', 'Tom']
>>> hashn=dict([('Tom','A'),('Jerry','B'),('Kim','A')])#declare method2
>>> hashn
{'Tom': 'A', 'Jerry': 'B', 'Kim': 'A'}
>>> hashm=dict(Tom=A,Jerry=B,Kim=A)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    hashm=dict(Tom=A,Jerry=B,Kim=A)
NameError: name 'A' is not defined
>>> hashm=dict(Tom='A',Jerry='B',Kim='A')#declare method3
>>> hashm
{'Tom': 'A', 'Jerry': 'B', 'Kim': 'A'}
```

### calculation
```
>>> 5+4
9
>>> 5-4
1
>>> 5/4
1.25
>>> 5*4
20
>>> 5//4
1
>>> 5%4
1
>>> 6%4
2
>>> 5^4
1
>>> 2**5
32
>>> 4/2
2.0
>>> 4//2
2
>>> pow(27,1/3)
3.0
>>> pow(8,1/3)
2.0
>>> pow(-2,1/2)
(8.659560562354934e-17+1.4142135623730951j)
>>> import cmath
>>> cmath.sqrt(5)
(2.23606797749979+0j)
>>> cmath.sqrt(-1)
1j
>>> cmath.sqrt(-5)
2.23606797749979j
>>> pow(-5,1/2)
(1.3691967456605067e-16+2.23606797749979j) 
```

### string and operator
```
>>>print ("str"+'ing','operator'*2)
string operatoroperator
>>>e,f="hello",'hello'
>>> print (e[0]+e[3])
hl
>>> print(e[0:3])
hel
>>> print(e[-1:-3])

>>> print(e[-3:-1])
ll 
>>> print(e[-5:-3])
he
```

### working in shell
```
>>> b=0
>>> while(b<9):
	print(b)
	b=b+1

	
0
1
2
3
4
5
6
7
8

>>> if(b<10):
	print(b)

	
9
>>> if(b<10)
SyntaxError: invalid syntax


#for
>>> for i in range(5,9):
	print(i)

	
5
6
7
8
```

* break, perl last
* countinue, perl next
* pass, do nothing waiting for crtl+C;
