# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    pisano = [0,1]
    for i in range(1, n):
        previous, current = current, (previous + current) % m
        pisano.append(current)
        if previous == 0 and current == 1:
            m = i
            break
    p = n % m
    return pisano[p]
if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
