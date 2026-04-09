import numpy as np


def binary_search(L, X):
    low = 0
    high = len(L) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        
        if L[mid] == int(X):
            return mid  # Found target, return its index
        elif L[mid] < int(X):
            low = mid + 1  # Target is in the right half
        else:
            high = mid - 1  # Target is in the left half
            
    return -1  # Target not found


arr = [1,2,3,4,5,6,7,8,9,10]
print("Arreglo:",arr) 
y=input("Que numero quiere buscar:")
x=binary_search(arr,y)
if x>=0:
    print("Elemento ",y,  " encontrado en la posicion:",x)
else:
    print("El elemento ",y, " no se encuentra")