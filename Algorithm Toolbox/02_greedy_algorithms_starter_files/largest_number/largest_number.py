#Uses python3
import sys


def largest_number(a):
    #write your code here
    a = sorted(a, reverse=True)
    max_digit = a[0]
    for i in range(len(a)-1):
       max_digit = get_greater(max_digit, a[i + 1])
    return max_digit


def get_greater(a,b):
    A = int(str(a) + str(b))
    B = int(str(b) + str(a))
    if A >= B:
        return A
    if A < B:
        return B

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
