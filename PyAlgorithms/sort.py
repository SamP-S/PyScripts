import random as r
import time

# optimised bubble sort
# https://en.wikipedia.org/wiki/Bubble_sort
# O(n^2)
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            l = i + j
            r = i + j + 1
            if lst[l] > lst[r]:
                temp = lst[l]
                lst[l] = lst[r]
                lst[r] = temp
    return lst

# merge sort
# https://en.wikipedia.org/wiki/Merge_sort
# O(n log n)
def merge_sort(lst):
    l = len(lst)
    if l == 1:
        return lst
    elif l == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return lst
    else:            
        midIndex = len(lst) // 2
        left = merge_sort(lst[0:midIndex])
        right = merge_sort(lst[midIndex:l])
        newLst = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                newLst.append(left.pop(0))
                if len(left) == 0:
                    newLst += right
            else:
                newLst.append(right.pop(0))
                if len(right) == 0:
                    newLst += left
        return newLst


if __name__ == "__main__":
    # experiment params
    METHOD = bubble_sort
    NAME = METHOD.__name__
    N = 1000
    DOMAIN = range(0, N)
    
    # unsorted
    print(f"Sorting: '{NAME}'")
    unsorted = r.sample(DOMAIN, N)
    
    # sorted with timing
    start_time = time.time()
    sorted = METHOD(unsorted)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")