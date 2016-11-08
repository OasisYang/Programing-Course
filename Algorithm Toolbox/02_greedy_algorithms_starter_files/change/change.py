# Uses python3
import sys

def get_change(m):
    #write your code here
    num_ten = int(m / 10)
    num_five = int((m - num_ten * 10) / 5)
    num_one = m % 5
    return num_ten+num_five+num_one

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
