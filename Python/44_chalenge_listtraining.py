#  Topic: Lists — one pass, O(n) time

# Problem statement
# Given a list of integers, 
# return a new list result where 
# result[i] is the sum of all elements from the start up to index i in the original list.

from typing import List

def running_sum(nums: List[int]) -> List[int]:
    total = 0
    result = []
    for num in nums:
            total += num
            result.append(total)
        
    return result 
    
nums = [3,2,5]
print(running_sum(nums))