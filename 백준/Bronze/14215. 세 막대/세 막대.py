import sys

a, b, c = map(int, sys.stdin.readline().split())

MAX = max(a, b, c)
SUM = (a + b + c) - MAX

if (MAX < SUM):
    print(a + b + c)
else:
    MAX = SUM - 1
    print(SUM + MAX)