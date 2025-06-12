import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort()

    cnt = 1
    next = lst[0][1]
    for i in range(1, n):
        if lst[i][1] < next:
            next = lst[i][1]
            cnt += 1
    print(cnt)