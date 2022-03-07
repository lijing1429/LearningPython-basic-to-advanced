# Basic concepts

The aim of this folder is to introduce all the basic concepts in python. 

## **1. Common sense**

- **Comments** for Class, Function and Syntax: Explain codes; make codes more readable.

- **Same Indentation** in codes: 'Tab' or 'two blankspace'
- **Global variables** inside function or class: avoid to use.

## **2. Name rules and conventions**

- **Syntax**: (underscore or letter) + (any number of letters, digits, or underscores)

- **Case matters**: ```A``` is not the same with ```a```

- **Reserved words should not be defined by users** (```True```, ```continue```,```break```, etc.)

- [**Conventions**](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions):

> Names rules: 

| Type | Name rules | Examples |
| ----------- | ----------- | ----------- |
| Package and Module Names | Short, all-lowercase name | ```pandas``` |
| Class Names | Normally use the CapWords convention | ```GoogleReq``` |
| Function and Variable Names | Lowercase, with words separated by underscores as necessary to improve readability | ```sum``` ,```string```|
| Constants | written in all capital letters with underscores separating words | ```MAX_OVERFLOW```,```TOTAL``` |


> Names to Avoid: 

Never use the single character below as variable names. ```l``` (for ```love```), ```O``` (for ```Opportunity```), ```I``` (for ```Ideal```)

> Special expression: 

| Syntax | Expression |  Applications |Description |
| ----------- | ----------- | ----------- |  ----------- |
| Single leading underscore | ```_X``` | only for non-public methods and instance variables| won't imported to new py files by a ```from module import *``` statement | 
| Single trailing underscore | ```X_``` |  used by convention to avoid conflicts with Python keyword| ```class_='ClassName'``` |
| Has two leading and trailing underscores | ```__X__``` | *system-defined* names |
| Begin with two underscores | ```__X``` | Used only to avoid name conflicts with attributes in classes designed to be subclassed | *Localized attributes* to classes. |
| Just a single underscore | ```_``` | use to express *Not using variables* |

## **3. Built-in Data type**

> ```type()``` to find out the variable's data type.

| Categories  | Type |  Examples |
| ------------- | ----------- | ----------- |
| Text Type | ```str``` | ```x = "Hello World"``` | 
| Numeric Types | ```int```, ```float```, ```complex``` | ```x = 1``` , ```x = 1.22``` , ```x = 1+2j```| 
| Sequence Types | ```list``` , ```tuple```, ```range``` | ```x = [1,2,'hello']``` , ```x = (1,2,'hello')``` , ```x = range(6)```| 
| Mapping Type | ```dict``` | ```x = {"name" : "John", "age" : 36}``` | 
| Set Types | ```set``` , ```frozenset``` | ```x = {"apple", "banana", "cherry"}``` , ```x = frozenset({"apple", "banana", "cherry"})``` | 
| Boolean Type | ```bool``` | ```x = True``` | 
| Binary Types | ```bytes``` , ```bytearray``` , ```memoryview```| ```x = b"Hello"``` , ```x = bytearray(5)``` , ```x = memoryview(bytes(5))```| 

> ```str```

- Slicing : ```a[2:5]``` , ```a[:5]```, ```a[2:]``` , ```a[-5:-2]```
- Modify : ```a.upper()``` , ```a.lower()``` , ```a.strip()``` , ```a.replace("H", "J")``` , ```a.split(",")```
- Concatenation : ```c = a+b```
- Format :  ```f'My name is {a}' ```

> Collections of data : ```list``` , ```tuple``` , ```set``` , ```dict```

- ```list``` : ordered (indexed by position) ,  changeable, allow duplicate values
- ```tuple``` : ordered (indexed by postion) ,  **unchangeable**, allow duplicate values
- ```set``` : **unordered (unindexed)** , **unchangeable**, **do not allow duplicate values**
- ```dict``` :  ordered (indexed by keys) , changeable and **do not allow duplicate keys**

> ```list```

- access items by the index number : ```list1[1]``` , ```list1[2:5]``` , ```list1[:5]``` , ```list1[2:]```
- change the list items :  ```list1[1] = 'strangers'```
- add list items : ```append()``` ,  ```insert()``` , ```extend()```
- remove list items : ```remove()``` , ```pop()``` , ```del``` , ```clear()```
- List Comprehension:  ```[x for x in fruits if "a" in x]``` , ```[x if x != "banana" else "orange" for x in fruits]```
- sort lists: ```list1.sort()``` , ```list1.reverse()```
- join lists: ```list1 + list2``` , ```list1.append(x)``` , ```list1.extend(list2)```
- notes: use ```copy``` and ```deepcopy``` to assign a new variable, in case changing the value directly to affect other variables.

> ```tuple```

- access items by the index number : ```tuple1[1]``` , ```tuple1[2:5]``` , ```tuple1[:5]``` , ```tuple1[2:]```
- change items by coverting into a list
- return many items in function: automatically create a tuple
- unpacking tuples :  ```(green, yellow, red) = tuple1``` , ```(green, yellow, *red) = tuple1``` , ```(green, *tropic, red) = tuple1``` (* means the left values will be assigned to this one)
- join tuples : ```tuple1 + tuple2``` , ```fruits * 2```

> ```set```

- access items: only by ```for``` loop. **Cannot** referring by index or key.
- add items :  one item - ```add()``` , any object - ```update()```
- remove set items : ```remove()``` , ```discard()``` , ```pop()``` , ```clear()``` , ```del()```
- join sets : ```union()``` , ```update()```

> ```dict```

- access items : by key name ```thisdict["model"]``` , ```get()``` , get keys ```thisdict.keys()``` , get values ```thisdict.values()``` , get all items ```thisdict.items()```
- change items : change values ```thisdict["year"] = 2018``` , ```update``` method
- remove items : ```pop()``` , ```popitem()```  , ```del``` , ```clear()```
- notes: use ```copy``` and ```deepcopy``` to assign a new variable, in case changing the value directly to affect other variables.


## **4. Operators**

| Operators Type | Description |
| ----------- | ----------- |
| Arithmetic Operators | ```+``` , ```-``` , ```*``` , ```/``` , ```%``` , ```**``` , ```//``` |
| Assignment Operators | ```=``` , ```+=``` , ```-=``` , ```*=``` , ```/=``` , ```%=``` , ```//=``` , ```**=``` , ```&=``` , ```^=``` , ```>>=``` , ```+=```|
| Comparison Operators | ```==``` , ```!=``` , ```>``` , ```>=``` , ```<``` , ```<=``` , ```\|=```||
| Logical Operators | ```and``` , ```or``` , ```not``` |
| Identity Operators | ```is``` , ```is not``` |
| Membership  Operators | ```in``` , ```not in``` |
| Bitwise  Operators | ```&``` , ```\|``` , ```^``` , ```~ ``` , ```<<``` , ```>>``` |

## **5. Basic statements**

> ```if ... else...```

- ```pass``` , ```return```

> ```while``` loop 

- ```continue``` , ```break``` , ```return``` , ```pass```
- you can use ```else``` if you want

> ```for``` loop 

- ```continue``` , ```break``` , ```return``` , ```pass```
- you can use ```else``` if you want

## **6. Functions**

> ```def``` 
- Arbitrary Arguments : ```*args```
- Arbitrary Keyword Arguments : ```**kwargs``` 
  
> ```lambda```
- Syntax : ```lambda arguments : expression```

> ```class/object```
- Syntax : ```class Person:```
-  ```__init__()``` :**all the class has this function**; executed when the class is being initiated; **assign values** to object properties
-  ```self``` : a reference to the current instance of the class ; It does not have to be named self , you can call it whatever you like.
  
> ```Child Class``` : 
- Syntax : ```class Student(Person):```
-  ```super()``` : make the child class inherit all the methods and properties from its parent
-  method in the child class has same name of parent class :  the inheritance of the parent method will be overridden.

## **7. Modules**
- ```import...(as)...``` ; ```from...import...```  :  the .py files
-  ```dir()``` : list all the function names (or variable names) in a module

## **8. Other information**
- **Regular expression** : ```re```
- **```try...except...else...finally...```** : catch all the errors **```Exception```**
- input data: ```input()```
- ```format``` 