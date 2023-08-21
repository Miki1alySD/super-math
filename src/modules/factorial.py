def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def factorial_norm(n):
    summa = 1
    for i in range(1, n + 1):
        summa *= i
    return summa
