"""
RackerRanck challenge Tuples
Given an integer, n, 
and n space-separated integers as input, create a tuple, , of those  integers. 
Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""

n = 1
x = "1 2" 
integer_list = map(int, x.split())
t = tuple(integer_list)
print(hash(t))