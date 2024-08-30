# TASK --- Hacker Rank
# You are given a two lists A and B. Your task is to compute their cartesian product A X B.
# Output Format
# Output the space separated tuples of the cartesian product.
# Sample imput:
    # 1 2
    # 3 4
# Sample Output
    # (1, 3) (1, 4) (2, 3) (2, 4)
# itertools.product()
    # This tool computes the cartesian product of input iterables.
    # It is equivalent to nested for-loops.
    # For example, product(A, B) returns the same as ((x,y) for x in A for y in B).


from itertools import product
# A = [1, 2]
# B = [3, 4]

# print(*tuple(product(A,B)))

a = "1 2"
b = "3 4"


A = [int(x) for x in a.split()]
B = [int(x) for x in b.split()]

# print(*product(A,B))

output = ""
for item in product(A, B):
    output += str(item) + " "

print(output)