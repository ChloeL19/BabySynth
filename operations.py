class Concat:
    '''
    x - string
    y - string
    returns concatenation of x and y
    '''
    num_args = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self, env=None):
        return f"({self.x}) + ({self.y})"

class GetFirst:
    '''
    x - string, or expression that evaluates to a string.
    returns first letter of the input string.
    '''
    num_args = 1

    def __init__(self, x):
        self.x = x
    
    def __str__(self, env=None):
        return f"({self.x})[0]"

class Title:
    '''
    x - string, or expression that evaluates to a string.
    returns x with the first letter capitalized.
    '''
    num_args = 1

    def __init__(self, x):
        self.x = x
    
    def __str__(self, env=None):
        return f"({self.x}).title()"

class Add:
    '''
    x - integer
    y - integer
    returns sum of x and y
    '''
    num_args = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} + {self.y}"

class Multiply:
    '''
    x - integer
    y - integer
    returns product of x and y
    '''
    num_args = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} * {self.y}"

class Divide:
    '''
    x - integer
    y - integer
    returns quotient of x and y
    '''
    num_args = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} / {self.y}"