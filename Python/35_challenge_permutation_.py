"""

There are two -element arrays of integers,  A and B . Permute them into some A' and  B' such that the relation  holds for all  where .

There will be q queries consisting of A, B , and K. For each query, return YES if some permutation A', B' satisfying the relation exists. Otherwise, return NO.

Example
A = [0, 1]
B = [0, 2]
K = 1
A valid  A', B'  is A' = [1,0] and B' = [0,2]: 1+0>= 1  and 0+2 .=1. Return YES.

Function Description

Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

twoArrays has the following parameter(s):

int k: an integer
int A[n]: an array of integers
int B[n]: an array of integers

"""

# TODO undestand better why sort reverse. 

A = [0, 1]
B = [0, 2]
k = 1


def twoArrays(k, A, B):
    
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


result = twoArrays(k, A, B)
print(result)

# permutations = list(itertools.product(A, B))
# print(permutations)