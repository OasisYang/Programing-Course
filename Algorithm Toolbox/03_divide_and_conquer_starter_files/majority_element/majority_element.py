# Uses python3
import sys


def get_majority_element(a):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     else:
#
#     return -1
    candidate, count = None, 0
    for e in a:
        if count == 0:
            candidate, count = e, 1
        elif e == candidate:
            count += 1
        else:
            count -= 1
    return count, candidate

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    count, majority = get_majority_element(a)
    i = 0
    for x in a:
        if x == majority:
            i += 1
    if i > len(a)//2:
        print(1)
    else:
        print(0)