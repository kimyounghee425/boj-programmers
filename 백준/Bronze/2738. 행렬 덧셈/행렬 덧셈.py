n, m = map(int, input().split())
a, b = [], []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

for i in range(n):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(n):
    for j in range(m):
        result = a[i][j] + b[i][j]
        print(result, end=" ")
    print()