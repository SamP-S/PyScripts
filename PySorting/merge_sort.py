# merge sort because its fast and recursive

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
    

unsortedLst = [14, 5, 32, 6, 11, 45, 21]
print(unsortedLst)
sortedLst = merge_sort(unsortedLst)
print(sortedLst)