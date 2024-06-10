"""Given an array a, your task is to output an array b of the same length by applying the following transformation:
- For each i from 0 to <a.length - 1> inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
- If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
- For instance, b[0] = 0 + a[0] + a[1] - challenge from code signal """

a = [4, 0, 1, -2, 3]

def solution(a):
    n = len(a)
    b = [0 for x in range(n)]
    for i in range(n):
        b[i]=a[i]
        if i > 0:
             b[i]+=  a[i-1]
        if i < n-1:
            b[i] += a[i+1]
    return b

print(solution(a))