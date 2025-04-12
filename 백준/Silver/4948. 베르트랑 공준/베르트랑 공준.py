import sys
from math import sqrt
 
input = sys.stdin.readline
# 에라토스테네스의 체로 123456까지의 모든 소수를 구하자
arr = [True for _ in range(2 * 123457)]
arr[0], arr[1] = False, False
for i in range(2, int(sqrt(2 * 123456)) + 1):
    if arr[i]:
        j = 2
        while i * j <= 2 * 123456:
            arr[i * j] = False
            j += 1
while 1:
    n = int(input())
    if n == 0:
        break
 
    cnt = arr[n + 1:2 * n + 1].count(True)
    print(cnt)