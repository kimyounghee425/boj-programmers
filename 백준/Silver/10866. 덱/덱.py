from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    order = input().split()
    cmd = order[0]

    if cmd == "push_front":
        x = order[1]
        d.appendleft(int(x))
    elif cmd == "push_back":
        x = order[1]
        d.append(int(x))
    elif cmd == "pop_front":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if d:
            print(d.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(d))
    elif cmd == "empty":
        if d:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd == "back":
        if d:
            print(d[-1])
        else:
            print(-1)