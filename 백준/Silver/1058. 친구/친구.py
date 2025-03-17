n = int(input())
graph = [list(input()) for _ in range(n)]
 
dist = [[1001]*n for _ in range(n)]
 
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
            continue
        if graph[i][j] == 'Y':
            dist[i][j] = 1
 
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]
 
ans = -1
for i in range(n):
    friend = 0
    for j in range(n):
        if 0 < dist[i][j] <= 2:
            friend += 1
    if ans < friend:
        ans = friend
 
print(ans)