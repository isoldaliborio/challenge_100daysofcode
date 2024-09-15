

def findMedian(arr):
    n = len(arr)
    arr.sort()
    midle_index = int(n/2)
    result = arr[midle_index]
    return result