x, y = map(int, input().split())
z = (y*100)//x

if z>98:
    print(-1)
    exit()
start = 0
end = x
while start<end:
    mid = (start+end)//2
    if (y+mid)*100//(x+mid) != z:
        end = mid
    else:
        start = mid + 1
mid = (start+end)//2
print(mid)