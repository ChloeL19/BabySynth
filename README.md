# BabySynth
A bottom-up synthesizer for two very small target languages.

# Usage
## For the Integer DSL
`python BabySynthArith.py [arg1, arg2, expected_answer] [arg1, arg2, expected_answer] [more input examples if necessary...]`

The target Arithmetic DSL is a super simple subset of python integer operations, i.e. [ADD, MULTIPLY, DIVIDE]. The DSL contains the following expressions and constants: [x, y, 0, 1, 2, 3].

Results are here: https://github.com/ChloeL19/BabySynth/blob/main/integer_samples.txt  

#### Command for Test Case 1:
`python BabySynthArith.py [1,1,2] [2,3,5] [7,4,11] [-1,1,0]`

#### Command for Test Case 2:
`python BabySynthArith.py [2,3,8] [1,2,5] [-1,2,3]`

#### Command for Test Case 3:
`python BabySynthArith.py [1,1,2] [0,-5,0] [8,10789,16]`

#### Command for Test Case 4:

#### Command for Test Case 5:

## For the String DSL
`python BabySynthString.py [arg1, arg2, expected_answer] [arg1, arg2, expected_answer] [more input examples if necessary...]`

The target String DSL is a super simple subset of python string operations, i.e. [CONCAT, GETFIRST (slice off the first letter of the string), TITLE (capitalize the first letter of the string)]. The DSL contains the following expressions and constants: [s1, s2, "\"a\"", "\"A\""].

Results are here: https://github.com/ChloeL19/BabySynth/blob/main/string_samples.txt

#### Command for Test Case 1:
`python BabySynthString.py [hi,H] [bye,B] [chloe,C]`

#### Command for Test Case 2:
`python BabySynthString.py [hi,Hi] [hey,Hey] [woo,Woo]`

#### Command for Test Case 3:
`python BabySynthString.py [cow,boy,Cowboy] [big,city,Bigcity] [hullah,baloo,Hullahbaloo]`

#### Command for Test Case 4:
`python BabySynthString.py [cow,boy,c] [big,city,b] [hullah,baloo,h]`

#### Command for Test Case 5:
`python BabySynthString.py [cow,boy,CB] [big,city,BC] [hullah,baloo,HB]`

This one takes a while! Great motivation for developing a better pruning and/or heuristics strategy, but alas I don't have time. The one tweak I did make is that on every iteration I reverse the order in which I traverse the operations list. This seemed to help a bit.

# Limitations
My code is not incredibly general; it is hard-coded in some sense to work with operations that expect a certain number of arguments. Also the way I pass environments to the evaluation function is kinda jank.
