import sys
def col(ch):
    return ord(ch)-ord('A')+1

def row(x):
    return 9-int(x)

def row_reverse(x):
    return str(9-x)

def col_reverse(x):
    return chr(x+ord('A')-1)

def ans(x):
    ans = ""
    ans += col_reverse(x[1])
    ans += row_reverse(x[0])
    return ans

def move(dir):
    if dir == "R": return (0, 1)
    elif dir == "L": return (0, -1)
    elif dir == "B": return (1, 0)
    elif dir == "T": return (-1, 0)
    elif dir == "RT": return (-1, 1)
    elif dir == "LT": return (-1, -1)
    elif dir == "RB": return (1, 1)
    else: return (1, -1)

    
king, stone, N = sys.stdin.readline().split()

k = [row(king[1]), col(king[0])]
s = [row(stone[1]), col(stone[0])]

for _ in range(int(N)):
    dir = move(sys.stdin.readline().strip())
    if 1 <= k[0]+dir[0] <= 8 and 1 <= k[1]+dir[1] <= 8:
        # 돌과 같은 곳으로 이동
        if s[0] == k[0]+dir[0] and s[1] == k[1]+dir[1]:
            if 1 <= s[0]+dir[0] <= 8 and 1 <= s[1]+dir[1] <= 8:
                s[0], s[1] = s[0]+dir[0], s[1]+dir[1]
                k[0], k[1] = k[0] + dir[0], k[1] + dir[1]
            else:
                continue
        else:
            k[0], k[1] = k[0]+dir[0], k[1]+dir[1]
    else:
        continue

print(ans(k))
print(ans(s))