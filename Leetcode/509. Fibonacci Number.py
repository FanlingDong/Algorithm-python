# 1 1 2 3 5 8 13....
# 1 normal method, O(2^n - 1) = O(2^n)
def fibonacci_1(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci_1(n-1) + fibonacci_1(n-2)


# reduce the complex level of fibonacci
# the input data structure should be changed as: first, second, n
# if n = 5, first = 2, second = 3
def fibonacci_2(first: int, second: int, n: int):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n == 3:
        return first + second
    else:
        return fibonacci_2(second, second + first, n - 1)


print(fibonacci_2(1, 1, 7))