RackerRanck

"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example list = [1,3,7,5,9]

The minimum sum is 1+3+7+5 =16  and the maximum sum is 3+7+5+9 = 24 . The function prints: 16 24"""

def miniMaxSum(arr):
    sorted_list = sorted(arr)
    minimum_sum = sum(sorted_list[:-1])
    maximum_sum = sum(sorted_list[1:])
    
    print(minimum_sum, maximum_sum)

#other possibilities:
# Using Reverse Iterator
# Using negative indexing
# Using list.pop()
# Using reversed() with next() 
# Using itemgetter