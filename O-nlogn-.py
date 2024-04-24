# O(n log n): Create an efficient sorting algorithm, such as merge sort or quicksort, that sorts a list of elements in nearly linear time.
import numpy as np

def ordenate(arr):
    
    if len(arr) <=1:
        return arr
    
    mid = len(arr) // 2
    left = ordenate(arr[:mid])
    right = ordenate(arr[mid:])

    return merge(left, right)

def merge(left, right):
    arr = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr.append(left[l])
            l += 1
        else:
            arr.append(right[r])
            r += 1

    arr.extend(left[l:])
    arr.extend(right[r:])
    return arr

arr = np.arange(1, 51)

np.random.shuffle(arr)

print('Shuffle Array: 'arr)
print('Ordenate Array: 'ordenate(arr))