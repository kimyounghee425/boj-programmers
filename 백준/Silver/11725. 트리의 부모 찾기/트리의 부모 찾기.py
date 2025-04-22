import sys

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()
        for i in graph[node]:
            parent[i].append(node)
            stack.append(i)
            graph[i].remove(node)

dfs(1)

for i in range(2, len(parent)):
    print(parent[i][0])