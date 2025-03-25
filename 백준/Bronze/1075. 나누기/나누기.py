n=input()
f=int(input())
p=int(n[:-2]+'00')
for i in range(100):
    if(p+i)%f==0:
        print(str(p+i)[-2:])
        break