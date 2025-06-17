from sys import stdin

def toggle(r,c):
    for i in range(r,r+3):
        for j in range(c,c+3):
            A[i][j] ^= 1
                
N,M = map(int,stdin.readline().split())
A = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int,stdin.readline().rstrip())) for _ in range(N)]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            toggle(i,j)
            cnt += 1

print(cnt if A == B else -1)