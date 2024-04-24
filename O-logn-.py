# O(log n): Develop a binary search algorithm that finds an element in a sorted list. This algorithm should halve the search space with each iteration.

def binary_search(arr, target):
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

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(binary_search(arr, 20))