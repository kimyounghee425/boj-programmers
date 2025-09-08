import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())

data = [[] for _ in range(n+1)]
q = deque()

def bfs(s,e):
    q.append(s)
    visited = [-1] * (n+1)
    visited[s] = 0
    while q:
        tmp = q.popleft()
        for node, d in data[tmp]:
            if visited[node] != -1:
                continue
            visited[node] = visited[tmp] + d
            if node == e:
                q.clear()
                return visited[e]
            else:
                q.append(node)
    return visited[e]


for _ in range(n-1):
    _s, _e, _d = map(int, input().split())
    data[_s].append((_e, _d))
    data[_e].append((_s,_d))

for _ in range(m):
    s,e = map(int, input().split())
    print(bfs(s,e))