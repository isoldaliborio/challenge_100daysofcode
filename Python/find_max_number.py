# Given a list of integers, create a function that returns the max value

def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

    # max_num = None

    # for num in nums:
    #     if max_num is None or num > max_num:
    #         max_num = num
    # return max_num

lst = [44, 7, 1, 0, 80, -9]

max = find_max(lst)

print(max)
