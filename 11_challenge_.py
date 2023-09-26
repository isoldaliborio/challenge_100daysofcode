"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.
"""

# inputs sample
a = 5
l = "23665"

arr = map(int, input(l).split())
arr = list(arr)
arr = [*set(arr)]
arr.sort(reverse = True)
print(arr[1]) 

