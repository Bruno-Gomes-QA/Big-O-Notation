# O(n): Implement an algorithm that traverses all elements of a list and returns the index of the searched element, if present.

def search_element(arr, target):
    if not arr:
        return 'Array is empty'
        
    for i, e in enumerate(arr):
        if e == target:
            return i

    return -1

arr = list(range(1,100))
print(search_element(arr, 100))