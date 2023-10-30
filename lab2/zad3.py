import unittest
import random
import matplotlib.pyplot as plt
from zad2 import mergesortParaller, mergesort
import time

def check_if_sorted(arr):
    for i in range(len(arr)-1):
        try:
            if arr[i + 1] < arr[i]:
                return False
        except:
            return False
    return True

class TestMultiprocessingMerge(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        self.array = [64, 50, 53, 0, 45, 37, 18, 21, 88, 78, 48, 62, 98, 84, 44, 57, 12, 96, 59, 81, 34, 7, 15, 42, 38, 60, 73, 94, 11, 71, 90, 35, 49, 1, 22, 51, 13, 83, 26, 92, 33, 54, 43, 39, 6, 69, 75, 70, 17, 79, 24, 23, 46, 29, 87, 95, 72, 9, 66, 40, 47, 89, 93, 27, 10, 19, 32, 99, 77, 55, 85, 76, 8, 16, 31, 4, 58, 41, 20, 65, 67, 52, 3, 80, 14, 25, 61, 91, 63, 74, 97, 36, 30, 28, 86, 5, 2, 68, 56, 82]
        super().__init__(methodName)

    def test_if_sorted_single(self):

        start = time.time()
        sorted_arr = mergesort(self.array)
        stop = time.time()
        print(f'single 100, time: {stop-start}')
        self.assertTrue(check_if_sorted(sorted_arr))

    def test_if_sorted(self):
        
        start = time.time()
        sorted_arr = mergesortParaller(self.array, 2)
        stop = time.time()
        print(f'parallel, 2 pools, time: {stop-start}')
        self.assertTrue(check_if_sorted(sorted_arr))

    def test_if_sorted_4(self):
        
        start = time.time()
        sorted_arr = mergesortParaller(self.array, 4)
        stop = time.time()
        print(f'parallel, 4 pools, time: {stop-start}')
        self.assertTrue(check_if_sorted(sorted_arr))

    def test_if_sorted_8(self):
        
        start = time.time()
        sorted_arr = mergesortParaller(self.array, 8)
        stop = time.time()
        print(f'parallel, 8 pools, time: {stop-start}')
        self.assertTrue(check_if_sorted(sorted_arr))

    def test_wrong_arr(self):
        arr = ['kotek', 'piesek', 2, 'inne', 'b']
        with self.assertRaises(TypeError):
            mergesortParaller(arr, 8)

if __name__ == '__main__':
    unittest.main()
