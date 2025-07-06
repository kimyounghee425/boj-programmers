import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = [0] * (n + 1)
count = 1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

data = [r]
while data:
    cur = data.pop(0)
    visited[cur] = True
    result[cur] = count
    count += 1

    for i in sorted(graph[cur], reverse=True):
        if not visited[i]:
            visited[i] = True
            data.append(i)

for i in result[1:]:
    print(i)