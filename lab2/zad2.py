from multiprocessing import Pool
import time, random, sys
import numpy as np

def merge(left, right):
    ret = []
    li = ri = 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append(right[ri])
            ri += 1
    if li == len(left):
        ret.extend(right[ri:])
    else:
        ret.extend(left[li:])
    return ret

def mergesort(lyst):
    if len(lyst) <= 1:
        return lyst
    ind = len(lyst)//2
    return merge(mergesort(lyst[:ind]), mergesort(lyst[ind:]))

def mergeWrap(AandB):
    a,b = AandB
    return merge(a,b)

#---------------------------------------------------------------------------

def mergeWrap(AandB):
    a,b = AandB
    return merge(a,b)

def mergesortParaller(arr, n):
    numproc = n
    #count array lengths for every pool
    endpoints = [int(x) for x in np.linspace(0, len(arr), numproc+1)]
    #create lists for every pool
    args = [arr[endpoints[i]:endpoints[i+1]] for i in range(numproc)]
        
    #create pools
    #assign  merge sort  for every pool 
    with Pool() as p:
        sortedsublists = p.map(mergesort, args)

    while len(sortedsublists) > 1:
        #get sorted sublist pairs to send to merge
        args = [(sortedsublists[i], sortedsublists[i+1]) \
                for i in range(0, len(sortedsublists), 2)]
        
        with Pool() as p:
            sortedsublists = p.map(mergeWrap, args)

    return sortedsublists[0]
