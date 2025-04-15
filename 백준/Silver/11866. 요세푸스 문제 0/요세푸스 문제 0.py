n,k = map(int,input().split())
from collections import deque
circle = []
for i in range(n):
    circle.append((i+1,i))
queue = deque(circle)
result = []
answer = "<"
while queue:
    length = len(queue)
    a,b  = queue.popleft()
    if b%k == k-1:
        result.append(a)
    else:
        queue.append((a,b+length))
    
a = ", ".join(str(i) for i in result)
answer = answer+a+">"
print(answer)