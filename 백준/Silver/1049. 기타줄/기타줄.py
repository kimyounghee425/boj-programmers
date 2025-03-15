import sys

input = sys.stdin.readline

n, m = map(int, input().split())
set = []
single = []

for _ in range(m):
  a,b = map(int, input().split())
  set.append(a)
  single.append(b)

quotient = n // 6
remainder = n % 6
set_compare = []
single_compare =[]

result = 0
if quotient > 0:
  for i in range(m):
    set_compare.append(set[i])
    set_compare.append(single[i]* 6)
  result += min(set_compare) * quotient

for i in range(m):
  single_compare.append(set[i])
  single_compare.append(single[i]* remainder)
result += min(single_compare)

print(result)