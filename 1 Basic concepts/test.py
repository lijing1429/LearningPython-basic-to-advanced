# 1. comments
# line comments
print("Hello, World!") # line comments

class Examples:
    """function, class comments"""
    def __init__(self):
        '''function, class comments'''
        pass

# 2. indetation
if True:
    pass # Tab for indetation

while True:
    pass # four blankspace for indetation


# 3. tuple
# return many items in function means automatically create a tuple
def tuple1():
    return 0,1

data1 = tuple1()
print(type(data1))

# 4. if else
a = 3
b = 6
# way 1 to express
if a ==b:
    print('a equal to b')
elif a>=b:
    print('a greater than b')
else:
    print('a lower than b')

# way 2 to express
print('a equal to b') if a == b else print('a greater than b') if a>=b else print('a lower than b')

# 5. child class
class Person:
    '''parent class'''
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class Student(Person):
    '''child class'''
    def __init__(self, fname, lname):
        # way 1:  to inherit the methods and properties from its parent
        Person.__init__(self, fname, lname)
        # way 2:  to inherit the methods and properties from its parent
        super().__init__(fname, lname)

# 6. try except
'''catch all the errors''' 
try:
    path = r'c:/123.txt'
    with open(path) as f:
        print(f)
except Exception as errorName:
    print(errorName)