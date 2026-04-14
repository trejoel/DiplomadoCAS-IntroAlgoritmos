import numpy as np


def maximoSubarregloCruce(arr, left, right, mid):
    # Find the maximum sum of the subarray that crosses the midpoint
    left_sum = float('-inf')
    right_sum = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
    current_sum = 0
    for j in range(mid + 1, right+1):
        current_sum += arr[j]
        if current_sum > right_sum:
            right_sum = current_sum
    return left_sum + right_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
mid = (0 + len(arr)) // 2
print(" Maximo subarreglo de cruce de {} es {}".format(arr,maximoSubarregloCruce(arr,0,len(arr)-1,mid)))
