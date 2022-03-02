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