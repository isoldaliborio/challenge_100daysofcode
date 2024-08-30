"""
Given an array of integers, where all elements but one occur twice, find the unique element.

"""

def lonelyinteger(a):
    for item in a:
        if a.count(item) == 1:
            return item


# Also you can do yourself the count:
# 
# def count(sequence, item):
#     count = 0
#     for element in sequence:
#         if element == item:
#             count += 1
#     return count