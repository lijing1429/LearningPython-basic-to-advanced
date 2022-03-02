# Basic concepts

The aim of this folder is to introduce all the basic concepts in python. 

## **Common sense**

- **Comments** for Class, Function and Syntax: Explain codes; make codes more readable.

- **Same Indentation** in codes: 'Tab' or 'two blankspace'

### **Name rules and conventions**:

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

### **Built-in Data type**:

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

- ```list``` : ordered (indexed) ,  changeable, allow duplicate values
- ```tuple``` : ordered (indexed) ,  **unchangeable**, allow duplicate values
- ```set``` : **unordered (unindexed)** , **unchangeable**, **do not allow duplicate values**
- ```dict``` :  ordered (key to index) , changeable and **do not allow duplicate keys**