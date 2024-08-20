
"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

Example

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
"""

def plusMinus(arr):
    list_size = len(arr)
    posive_numbers = 0
    negative_numbers = 0
    zeros = 0
    for number in arr:
        if number < 0:
            negative_numbers += 1
        elif number == 0:
            zeros += 1
        else:
            posive_numbers += 1
    
    positive_ratio = posive_numbers / list_size
    negative_ratio = negative_numbers / list_size
    zeros_ratio = zeros / list_size
    
    # Print the results with 6 decimal places
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zeros_ratio))