import timeit


def naive_gcd(a, b):
    gcd = 0
    for d in range(1, a + b):
        if a%d == 0 and b % d == 0:
            gcd = d
    return gcd

def euclidean_gcd(a, b):
    if b == 0:
        return a
    a_remainder = a % b
    return euclidean_gcd(b, a_remainder)

if __name__ == "__main__":
    a = 1653264
    b = 3918848
    start = timeit.default_timer()
    gcd = naive_gcd(a, b)
    end = timeit.default_timer()
    print(f'{end - start} to compute gcd of {a}, {b} = {gcd}')
    start1 = timeit.default_timer()
    gcd1 = euclidean_gcd(a, b)
    end1 = timeit.default_timer()
    print(f'{end1 - start1} to compute gcd of {a}, {b} = {gcd1}')
    