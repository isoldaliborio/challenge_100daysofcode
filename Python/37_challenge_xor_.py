"""
simplifyed explanatoion for XOR
XOR is a rule that tells us when to turn on a new light based on the states of these two switches. Here’s how it works:

If both switches are off (both are 0), the new light will be off (0).
If one switch is on (1) and the other is off (0), the new light will be on (1).
If both switches are on (1), the new light will be off (0).
So, XOR is like saying, "The new light will only be on if exactly one of the switches is on." If both switches are the same (both on or both off), the new light is off.


In this challenge, the task is:
to debug the existing code to successfully execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.

To know more about XOR Click Here

Debug the given function 'strings_xor' to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The input consists of two lines. 
The first line of the input contains the first string,s , 
and the second line contains the second string, t .


"""


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

s = input()
t = input()
print(strings_xor(s, t))



# Function before debbuging
# 
# def strings_xor(s, t):
#     res = ""
#     for i in range(len(s)):
#         if s[i] = t[i]:
#             res = '0';
#         else:
#             res = '1';

#     return res

# s = input()
# t = input()
# print(strings_xor(s, t))