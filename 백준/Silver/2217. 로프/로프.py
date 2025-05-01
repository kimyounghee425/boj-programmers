import sys

input = sys.stdin.readline
N = int(input())

rope = [int(input()) for _ in range(N)]
rope.sort()

ans = 0

for i in rope:

    if ans < i * N:
        ans = i * N

    N -= 1

print(ans)