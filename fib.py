#fib.py

import time
import matplotlib.pyplot as plt
from functools import lru_cache

FIB_LIMIT = 100
execution_times = [None] * (FIB_LIMIT + 1) #initialize an array of 101

def timer(func):
    def wrapper(n):

        start = time.perf_counter()
        res = func(n)
        end = time.perf_counter()
        elapsed_time = end-start

        execution_times[n] = elapsed_time
        print(f"Finished in {elapsed_time: .8f}s: f({n}) -> {res}")
        return res
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n - 1) + fib(n -2)



if __name__ == "__main__":
    fib(100)

    fib_indices = list(range(FIB_LIMIT + 1))
    plt.plot(fib_indices, execution_times)
    plt.savefig("fib_exec_times.png")
    plt.show()