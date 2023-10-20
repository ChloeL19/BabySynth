import sys

class Add:
    '''
    x - integer
    y - integer
    returns sum of x and y
    '''
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
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x} / {self.y}"

# parse input/output specifications as a list of [[x,y,ans]]
if len(sys.argv) > 1:
    input_lists = sys.argv[1:]
    processed_lists = []
    for input_list in input_lists:
        if input_list.startswith('[') and input_list.endswith(']'):
            input_list = input_list[1:-1].split(',')
            input_list = [int(i) for i in input_list]
            processed_lists.append(input_list)
        else:
            print("Please provide input/output example list in the format: [x,y,ans],[x',y',ans']")
            sys.exit()
    print(processed_lists)
else:
    print("Please provide input/output example lists as command line arguments.")
    sys.exit()
input_list = processed_lists

# helper function for determining functional equivalence
def evaluate_equiv(program1, program2):
    '''
    program1 - string representing first program
    program2 - string representing second program
    input_list - list of input/output examples
    returns True if program1 and program2 evaluate to the same output on all input/output examples, False otherwise
    '''
    for example in input_list:
        x, y, ans = example[0], example[1], example[2]
        try:
            if eval(program1.__str__()) != eval(program2.__str__()):
                return False
        except:
            return False
    return True

def evaluate_correctness(program):
    for example in input_list:
        x, y, ans = example[0], example[1], example[2]
        try:
            if eval(program.__str__()) != ans:
                return False
        except:
            return False
    return True

# Target language Arith: Add, Multiply, Divide operations and all real numbers approximated by flaots in Python.
ops = [Add, Multiply, Divide]
expr = ["x", "y", "1", "0", "2", "3"] # values and constants in the language

PB = [] # the program bank
PB.extend(expr) # start with just level 1 expressions

# iterate through program bank and create the next level of programs
counter = 0
while len(PB) > 0:
    # find all pairs of arguments
    pairs = []
    for i in range(len(PB)):
        for j in range(i+1, len(PB)):
            pair = (PB[i], PB[j])
            reverse_pair = (PB[j], PB[i])
            if pair not in pairs and reverse_pair not in pairs:
                pairs.append(pair)
    # apply every possible operation to these pairs to get next generation
    for op in ops:
        for args in pairs:
            new_prog = op(args[0], args[1])
            if evaluate_correctness(new_prog):
                print("ans here:")
                print(new_prog.__str__())
                sys.exit()
            append = True
            # filter next generation for functionally equivalent programs on the test cases
            # NOTE: not a perfect pruning strategy if the test cases are bad, may remove the correct program
            for p in PB:
                if evaluate_equiv(p, new_prog):
                    append = False
            if append:
                PB.append(new_prog)

    # continue doing this process until we find a program that satisfies all of the user-given test cases
    counter += 1
