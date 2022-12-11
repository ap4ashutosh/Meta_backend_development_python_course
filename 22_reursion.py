import time

# t = time.time()
#
#
# def fac_by_rec(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac_by_rec(n - 1)
#
#
# t = time.time() - t
# print(t)
#
# a = fac_by_rec(100)
# print(a)
#
t1 = time.time()


def fac_by_loop(n):
    if n == 0:
        return 1
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


t1 = time.time() - t1
print(t1)

a = fac_by_loop(4299)
print(a)
