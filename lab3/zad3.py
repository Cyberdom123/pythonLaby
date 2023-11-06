import timeit
from functools import lru_cache


# Without lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# With lru_cache
@lru_cache(maxsize=2**10)
def fibonacci_cached(n):
    if n <= 1:
        return n
    else:
        return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


# Measure time
N = 35  # Example value
time_without_cache = timeit.timeit("fibonacci(N)", globals=globals(), number=1)
time_with_cache = timeit.timeit("fibonacci_cached(N)", globals=globals(), number=1)

print(f"Time taken to compute the {N}th Fibonacci number without cache: {time_without_cache} seconds")
print(f"Time taken to compute the {N}th Fibonacci number with cache: {time_with_cache} seconds")