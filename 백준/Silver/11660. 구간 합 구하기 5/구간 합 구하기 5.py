from sys import stdin
 
n,m=map(int,stdin.readline().split())
a=[[0 ]*(n+1) ]
for i in range(n) :
  b= list(map(int,stdin.readline().split()))
  b.insert(0,0)
  a.append(b)
#print(a)
 
#for i in range (n+1):
 # print(a[i])
 
for i in range (n+1) :
  for j in range (1,n+1) :
    a[i][j]+=a[i][j-1]
 
for i in range (1,n+1) :
  for j in range (n+1) :
    a[i][j]+=a[i-1][j]
 
#for i in range (n+1):
 # print(a[i])
 
for i in range (m) :
  x1,y1,x2,y2=map(int,stdin.readline().split())
  ans= a[x2][y2] - a[x1 -1 ][y2] - a[x2][y1-1] + a[x1-1][y1-1]
  print(ans)