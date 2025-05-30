import sys
n=int(sys.stdin.readline())
num=0
while num**2<n:
    num+=1
    if n==1:
        print(n)
        break
    elif num**2>=n:
        print(num-1)
    else:
        pass