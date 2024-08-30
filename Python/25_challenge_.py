"""
list comprehention. 

Let's learn about list comprehensions! You are given three integers x, y and z 
representing the dimensions of a cuboid along with an integer n . 
Print a list of all possible coordinates given by (i, j , k) on a 3D grid where the sum of  i+j+k is not equal to n. Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
"""

x = 1
y = 2
z = 3
n = 3
    
    

result = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(result)