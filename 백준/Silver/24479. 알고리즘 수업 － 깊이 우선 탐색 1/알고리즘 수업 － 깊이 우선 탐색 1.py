import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
N,M,R = map(int,input().split())
graph = [[] for _ in range(N+1)]
path = [0] * (N+1)
visited = [False] * (N+1)
cnt = 1

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(start):
    global cnt
    visited[start] = True
    path[start] = cnt
    graph[start].sort()
    for i in graph[start]:
        if visited[i] == False:
            cnt += 1
            DFS(i)
DFS(R)

for i in range(1,len(path)):
    print(path[i])