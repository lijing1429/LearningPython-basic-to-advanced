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

