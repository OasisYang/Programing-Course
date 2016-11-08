# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current = 1
    m = (from_-1 + 2) % 60
    n = (to + 2) % 60
    for _ in range(m - 1):
        previous, current = current, (previous + current) % 10
    a = current
    for _ in range(n-m):
        previous, current = current, (previous + current) % 10

    return (current - a) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
