# O(1): Write an algorithm that returns the first element of a list, regardless of the size of the list.

def first_element(arr):
    if not arr:
        return 'Array is empty'

    return arr[0]

arr = list(range(1,101))
print(first_element(arr))