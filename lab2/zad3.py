import unittest
import random
import matplotlib.pyplot as plt
from zad2 import multiprocessing_merge_sort

def check_if_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i + 1] < arr[i]:
            return False

    return True

def plot_arrays(arrays):
    for i in range(len(arrays)):
        print(i)
        plt.stem(arrays[i])
        plt.show()
class TestMultiprocessingMerge(unittest.TestCase):

    def test_if_sorted_100(self):
        arr = list(range(100))
        random.shuffle(arr)
        sorted_arr = multiprocessing_merge_sort(arr)
        self.assertTrue(check_if_sorted(sorted_arr))

    def test_if_sorted_1000(self):
        arr = list(range(1000))
        random.shuffle(arr)
        sorted_arr = multiprocessing_merge_sort(arr)
        self.assertTrue(check_if_sorted(sorted_arr))


if __name__ == '__main__':
    arr = list(range(100))
    random.shuffle(arr)
    sorted_arr1 = multiprocessing_merge_sort(arr)

    arr = list(range(1000))
    random.shuffle(arr)
    sorted_arr2 = multiprocessing_merge_sort(arr)

    listOfArrays = [sorted_arr1, sorted_arr2]
    plot_arrays(listOfArrays)
    
    unittest.main()
