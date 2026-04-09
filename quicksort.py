import numpy as np

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


arr = np.random.randint(100, size=10) 
#arr=[1,2,3,4,5,6,7,8,9,10]
#arr=[10,9,8,7,6,5,4,3,2,1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)