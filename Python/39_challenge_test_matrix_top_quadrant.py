
"""
The problem involves flipping rows and columns in a 2n x 2n matrix to maximize the sum of elements in the upper-left n x n submatrix. The game allows reversing rows or columns any number of times to achieve the maximum sum.
Explanation:
The matrix is 2n x 2n, and we want to maximize the sum of the top-left n x n submatrix.
For each element in the top-left n x n submatrix, there are four possible values (due to flipping rows/columns).
We compare these four possible values and take the maximum for each position to maximize the sum.
This approach ensures we maximize the sum by always selecting the highest possible value that can be achieved via flipping rows and/or columns.

In this example, the output is 414 as explained in the images.



Here’s a Python solution to solve the problem:

"""


def flippingMatrix(matrix):
    n = len(matrix) // 2  # n is half of the 2n size

    max_sum = 0

    # Loop over the top-left quadrant of the matrix
    for i in range(n):
        for j in range(n):
            # For each position in the n x n matrix, we consider the four possible candidates:
            # 1. matrix[i][j] (top-left quadrant)
            # 2. matrix[i][2*n - j - 1] (top-right quadrant)
            # 3. matrix[2*n - i - 1][j] (bottom-left quadrant)
            # 4. matrix[2*n - i - 1][2*n - j - 1] (bottom-right quadrant)
            
            # We take the maximum of these four to maximize the sum
            max_sum += max(matrix[i][j], 
                           matrix[i][2*n - j - 1], 
                           matrix[2*n - i - 1][j], 
                           matrix[2*n - i - 1][2*n - j - 1])

    return max_sum

# Example usage:
matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

result = flippingMatrix(matrix)
print(result)  # Output: 414




def flippingMatrix(matrix):
    n = len(matrix) // 2  # n is half the size of the matrix (since the matrix is 2n x 2n)

    max_sum = 0  # To store the maximum sum

    # Loop over the top-left n x n quadrant
    for i in range(n):
        for j in range(n):
            # Identify the four possible values for the current position (i, j):
            top_left = matrix[i][j]  # The element in the top-left quadrant
            top_right = matrix[i][2*n - j - 1]  # The element in the top-right quadrant
            bottom_left = matrix[2*n - i - 1][j]  # The element in the bottom-left quadrant
            bottom_right = matrix[2*n - i - 1][2*n - j - 1]  # The element in the bottom-right quadrant

            # Choose the largest value among the four
            max_sum += max(top_left, top_right, bottom_left, bottom_right)

    return max_sum  # Return the maximum possible sum