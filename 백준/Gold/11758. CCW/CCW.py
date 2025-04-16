import sys

f = sys.stdin

points = [list(map(int,f.readline().rstrip().split())) for _ in range(3)]

x1,y1 = points[0]
x2,y2 = points[1]
x3,y3 = points[2]

if (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) > 0:
    print(-1)
elif (x3-x1)*(y2-y1) - (y3-y1)*(x2-x1) == 0:
    print(0)
else:
    print(1)