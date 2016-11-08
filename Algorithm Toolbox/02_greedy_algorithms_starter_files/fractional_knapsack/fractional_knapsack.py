# Uses python3
import sys
import numpy as np


def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    W = capacity

    value_per_weight = values / weights
    weights_sort = [list(value_per_weight).index(x) for x in sorted(value_per_weight, reverse=True)]
    for i in range(len(values)):
        if W == 0:
            return value
        a = min(weights[weights_sort[i]], capacity)
        value = value + a * value_per_weight[weights_sort[i]]
        W = W - a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = np.array(data[0:2])
    values = np.array(data[2:(2 * n + 2):2])
    weights = np.array(data[3:(2 * n + 2):2])
    for i in range(len(values)):
        if weights[i] == 0:
            np.delete(weights, i, axis=0)
    # print(type(values))
    # print(type(weights))
    # print(values / weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
