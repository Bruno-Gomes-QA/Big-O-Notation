# O(log n): Develop a binary search algorithm that finds an element in a sorted list. This algorithm should halve the search space with each iteration.

def binary_search(arr, target):

    if not arr:
        return 'Array is empty'
        
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if target == arr[mid]:
            return mid  
        elif target < arr[mid]:
            right = mid - 1 
        else:
            left = mid + 1 
            
    return -1  

arr = list(range(1,100))
print(binary_search(arr, 20))