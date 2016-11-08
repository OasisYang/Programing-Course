# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    start =[]
    end = []
    start.append(start)
    end.append(start)
    i = 0
    p = 0
    #write your code here
    while i <= len(segments):
        if int(end[p]) >= segments[i+1].start:
            start[p] = min(segments[i+1].start,start[i])
            end[p] = max(segments[i+1].end,end[i])
        else:
            p += 1
            start.append(segments[i + 1].start)
            end.append(segments[i + 1].end)
    for _ in start:
        points.append(start)
        points.append(end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    print(len(segments))
    print(segments[0])
    # points = []
    # for s in segments:
    #     print(s)
    #     points.append(s.start)
    #     points.append(s.end)
    # print(points)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
