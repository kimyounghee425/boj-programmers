
l = [0, 1, 0, 0]
for _ in range(int(input())):
    x, y = map(int, input().split())
    l[x], l[y] = l[y], l[x]
print(l.index(1))