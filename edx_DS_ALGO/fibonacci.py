import functools
from timeit import default_timer as timer

def run_time(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        stop = timer()
        print(f'Run time of {func.__name__} is {stop - start} seconds')
        return result
    return wrapper


@run_time
def fib_recur(n):
    """
    Simple Recurssive algorithm to calculate fibonacci
    It is not efficient as run time is too long
    """
    def _fib_recur(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return _fib_recur(n -1) + _fib_recur(n -2)
    return _fib_recur(n)

@run_time
def fib_efficient(n):
    """
    Algorithm to calculate fibinacci using list.
    We store fibonacci numbers in list
    Runtime is small
    """
    ls = [0, 1]
    for i in range(2, n+1):
        num = ls[i - 1] + ls[i - 2]
        ls.append(num)
    return ls[n]

# start1 = timeit.default_timer()
# fib_n1 = fib_recur(50)
# end1 = timeit.default_timer()
# print(f'Fibbonaci recur {fib_n1} took time {end1 - start1}')

# start = timeit.default_timer()
# fib_n = fib_efficient(100000)
# end = timeit.default_timer()
# print(f'Fibbonaci effective {fib_n} took time {end - start}')
if __name__ == "__main__":
    fib_recur(30)
    fib_efficient(30)



