import sys

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

# parse input/output specifications as a list of [[x,y,ans], [x,ans]]
if len(sys.argv) > 1:
    input_lists = sys.argv[1:]
    processed_lists = []
    for input_list in input_lists:
        if input_list.startswith('[') and input_list.endswith(']'):
            input_list = input_list[1:-1].split(',')
            processed_lists.append(input_list)
        else:
            print("Please provide input/output example list in the format: [x,y,ans] or [x',ans']")
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
        args = example[:-1]  # Get the arguments from the example
        ans = example[-1]  # Get the expected answer from the example
        try:
            if len(args) == 2:
                x = args[0]
                y = args[1]
            elif len(args) == 1:
                x = args[0]
                y = ""
            else:
                return False
            if eval(program1.__str__()) != eval(program2.__str__()):
                return False
        except:
            return False
    return True

def evaluate_correctness(program):
    for example in input_list:
        args = example[:-1]  # Get the arguments from the example
        ans = example[-1]  # Get the expected answer from the example
        try:
            if len(args) == 2:
                x = args[0]
                y = args[1]
            elif len(args) == 1:
                x = args[0]
                y = ""
            else:
                return False
            if eval(program.__str__()) != ans:
                # print("program tried:")
                # print(program.__str__())
                return False
        except:
            return False
    return True

# Target language Strings: Concat, GetFirst (extract first letter), Title (capitalize first letter)
ops = [Concat, GetFirst, Title]
expr = ["x", "y", "\"a\"", "\"A\""] # values and constants in the language

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
    level = PB.copy()
    # apply every possible operation to these pairs to get next generation
    for op in ops:
        # treat each op differently based on the number of arguments it accepts
        if op.num_args == 1:
            for arg in level:
                new_prog = op(arg)
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
        else: # every operation has only either 1 or 2 arguments
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
    ops.reverse()
    # continue doing this process until we find a program that satisfies all of the user-given test cases
    counter += 1