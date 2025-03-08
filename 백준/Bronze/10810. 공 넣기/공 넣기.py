n, m = map(int, input().split())
answer = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for index in range(i,j+1):
        answer[index-1] = k

print(' '.join(str(n) for n in answer))