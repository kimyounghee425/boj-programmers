import sys

N = int(sys.stdin.readline())

xlist = list()
ylist = list()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xlist.append(x)
    ylist.append(y)
    
xlen = max(xlist) - min(xlist)
ylen = max(ylist) - min(ylist)

print(xlen * ylen)