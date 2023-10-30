from heapq import merge
import random
import multiprocessing

def multiprocessing_merge_sort(m, send_end=None):
    if len(m) < 2:
        result = m
    else:
        middle = len(m) // 2 #Floor division

        inputs = [m[:middle], m[middle:]]
        pipes = [multiprocessing.Pipe(False) for _ in inputs]

        processes = [multiprocessing.Process(target=multiprocessing_merge_sort,
                     args=(input, send_end))
                    for input, (recv_end, send_end) in zip(inputs, pipes)]
        for process in processes: process.start()
        for process in processes: process.join()

        results = [recv_end.recv() for recv_end, send_end in pipes]
        result = list(merge(*results))

    if send_end:
        send_end.send(result)
    else:
        return result
