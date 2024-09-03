""" 
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal 1+5+9 = 15  . The right to left diagonal 3+5+9 = 17 . 
Their absolute difference is 15 -17 = 2 .

Function description

Complete the  function 'diagonal difference' in the editor below.

diagonalDifference takes the following parameter:

    int arr[n][m]: an array of integers

Return

    int: the absolute diagonal difference

"""


n = 3
data = ("11 2 4" "4 5 6" "10 8 -12")

arr = []

for _ in data:
    arr.append(list(map(int, data.rstrip().split())))
print(arr)

def diagonalDifference(arr):
    left_diagonal = []
    right_diagonal = []
    count_left = 0
    count_right = len(arr)
    for row in arr:
        ld = row[count_left]
        rd = row[count_right -1]
        left_diagonal.append(ld)
        right_diagonal.append(rd)
        count_left += 1
        count_right -= 1

        difference = abs(sum(left_diagonal)-sum(right_diagonal))
    return difference

    result = diagonalDifference(arr)
    # print(result)


# Another solution
# def diagonalDifference(arr):
#     left_diagonal = []
#     right_diagonal = []
#     n = len(arr)

#     for i in range(n):
#         ld = arr[i][i]  # Left-to-right diagonal element
#         rd = arr[i][n - i - 1]  # Right-to-left diagonal element
#         left_diagonal.append(ld)
#         right_diagonal.append(rd)
        
#     difference = abs(sum(left_diagonal) - sum(right_diagonal))
#     return difference