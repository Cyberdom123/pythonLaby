import random
import numpy as np
import matplotlib.pyplot as plt

def check_if_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i + 1] < arr[i]:
            return False

    return True

def bubble_sort(arr):
    tmp = 0
    while not check_if_sorted(arr):
        for i in range(len(arr)-1):
            if arr[i + 1] < arr[i]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp

def select_sort(arr):
    tmp = min(arr)
    for i in range(len(arr)-1):
        if(arr[i] != tmp):
            arr[i] = tmp
        tmp = min(arr[i:])



N = 1000

arr = np.random.rand(N)
plt.stem(arr)
plt.show()
#bubble_sort(arr)
select_sort(arr)
plt.stem(arr)
plt.show()
