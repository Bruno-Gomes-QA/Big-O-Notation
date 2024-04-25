#O(n²): Desenvolva um algoritmo de ordenação ineficiente, como o bubble sort, que ordene uma lista de elementos em tempo quadrático.
# O(n²): Develop an inefficient sorting algorithm, such as bubble sort, that sorts a list of elements in quadratic time.

import numpy as np 

def ordenate(arr):
    
    l = len(arr)

    for a in range(l):
        for n in range(0, l-a-1):
            if arr[n] > arr[n+1]:
                arr[n], arr[n+1] = arr[n+1], arr[n]
    
    return arr

arr = np.arange(1,21)
np.random.shuffle(arr)

print(ordenate(arr))