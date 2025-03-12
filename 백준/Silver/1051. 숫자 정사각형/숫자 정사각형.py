import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
max_size = 1
for i in range(n):
    for j in range(m):
        for k in range(max_size,50):
            if n<=i+k or m<=j+k:
                break
            if len(set([board[i][j],board[i+k][j],board[i][j+k],board[i+k][j+k]])) == 1:
                max_size = max(max_size,k+1)
print(max_size**2)