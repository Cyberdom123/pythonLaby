import unittest
import random
import numpy as np
import matplotlib.pyplot as plt
from zad2 import mergesortParaller, mergesort
import time


if __name__ == '__main__':
    times = []
    timeSingle = []

    for i in range(100):
        arr = list(range(1000 * i))
        random.shuffle(arr)
        arr_cpy = arr;
        
        start = time.time()
        sotedArr = mergesortParaller(arr, 8)
        stop = time.time()
        times.append(float(stop-start))

        start = time.time()
        sotedArr = mergesort(arr_cpy)
        stop = time.time()
        timeSingle.append(float(stop-start)) 

    processes = np.linspace(1000, 100000, 100)
    plt.plot(processes, times, label='mergesortParaller')
    plt.plot(processes, timeSingle, label='mergesort')
    plt.xlabel('arrLength')
    plt.ylabel('time')
    plt.title("using 8 pools")
    plt.legend()
    plt.show()