# Basic concepts

The aim of this folder is to introduce all the basic concepts in python. 

## **Common sense**

- **Comments** for Class, Function and Syntax: Explain codes; make codes more readable.

- **Same Indentation** in codes: 'Tab' or 'two blankspace'

## **Name rules and conventions**:
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






