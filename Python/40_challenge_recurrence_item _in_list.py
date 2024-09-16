
"""

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

"""

ar = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38, 22, 44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]


def sockMerchant(items, numbers):
    list_set = set(ar)
    occurrences_by_color = []
    for iten in list_set:
        x = numbers.count(iten)
        if x%2 == 0:
            x=x/2
        elif x%2 == 1:
            x=(x-1)/2
        occurrences_by_color.append(int(x))

    return sum(occurrences_by_color)


result = sockMerchant(100, ar)
print(result)
