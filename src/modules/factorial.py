def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

# factorial_rec(5)
# 5 * factorial_rec(4) ---- 5 * 4 * 3 * 2 * 1
# factorial_rec(4)
# 4 * factorial_rec(3) ---- 4 * 3 * 2 * 1
# factorial_rec(3)
# 3 * factorial_rec(2) ---- 3 * 2 * 1
# factorial_rec(2)
# 2 * factorial_rec(1) ---- 2 * 1
# 1