a,b=0,0
d={'A+':4.5,'A0':4,'B+':3.5,'B0':3,'C+':2.5,'C0':2,'D+':1.5,'D0':1,'F':0}
for i in range(20):
    _,x,y=input().split()
    x=float(x)
    if y != 'P':
        a+=x
        b+=x*d[y]
print(b/a)