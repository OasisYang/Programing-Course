# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1
    m = (n+2) % 60
    for _ in range(m - 1):
        previous, current = current, (previous + current) % 10
        if current == 0:
            current = 10
    return current - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
