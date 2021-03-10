# optimised bubble sort for sorting

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


unsortedLst = [14, 5, 32, 6, 11, 45, 21]
print(unsortedLst)
sortedLst = bubble_sort(unsortedLst)
print(sortedLst)