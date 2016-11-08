# Uses python3
import sys
import numpy as np
def optimal_weight(W, w):
    # write your code here
    value = np.zeros((W+1, len(w)+1), dtype=int)
    i=0
    for x in w:
        i += 1
        for j in range(1, W+1):
            value[j, i] = value[j, i-1]
            if x <= j:
                val = value[j - x, i-1] + x
                if value[j, i] < val:
                    value[j, i] = val
    return value[W, len(w)]

    # for i in range(1, W+1):
    #     value[i] = 0
    #     for x in w:
    #         if x <= i:
    #             val = value[i - x] + x
    #             if val > value[i]:
    #                 value[i] = val
    # return value[W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
