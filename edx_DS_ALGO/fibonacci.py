import timeit


def fib_recur(n):
    """
    Simple Recurssive algorithm to calculate fibonacci
    It is not efficient as run time is too long
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n -1) + fib_recur(n -2)

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

start1 = timeit.default_timer()
fib_n1 = fib_recur(50)
end1 = timeit.default_timer()
print(f'Fibbonaci recur {fib_n1} took time {end1 - start1}')

start = timeit.default_timer()
fib_n = fib_efficient(100000)
end = timeit.default_timer()
print(f'Fibbonaci effective {fib_n} took time {end - start}')



