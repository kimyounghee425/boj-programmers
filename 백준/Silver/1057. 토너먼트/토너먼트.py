n, han, jimin = map(int, input().split())
answer = 0

while han != jimin:
    han -= han//2
    jimin -= jimin//2
    answer += 1

print(answer)