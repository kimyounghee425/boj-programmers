e,s,m=map(int,input().split())
result,tmp=0,0
while True:
    result=s+tmp*28
    E_mod=15 if result%15==0 else result%15		
    M_mod=19 if result%19==0 else result%19
    if E_mod==e and M_mod==m:break
    tmp+=1
print(result)