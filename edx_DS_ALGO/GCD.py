import functools
from timeit import default_timer as timer

def elapsed_time(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        print(f'Runtime for {func.__name__} is {end - start}')
        return result
    return wrapper

@elapsed_time
def naive_gcd(a, b):
    gcd = 0
    for d in range(1, a + b):
        if a%d == 0 and b % d == 0:
            gcd = d
    return gcd


@elapsed_time
def euclidean_gcd(a, b):
    def _euclidean_gcd(a, b):
        if b == 0:
            return a
        a_remainder = a % b
        return _euclidean_gcd(b, a_remainder)
    return _euclidean_gcd(a, b)

if __name__ == "__main__":
    a = 1653264
    b = 3918848
    naive_gcd(a, b)
    euclidean_gcd(a, b)
    
    