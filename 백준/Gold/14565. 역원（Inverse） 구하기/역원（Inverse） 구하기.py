import sys
input = sys.stdin.readline

n, a = map(int, input().split())

def gcd(a,b):
    if b == 0 : return a
    return gcd(b, a%b)

def xgcd(a,b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    
    while True:
        q = r1 // r2
        r = r1 - (q*r2)
        s = s1 - (q*s2)
        t = t1 - (q*t2)
                
        if r == 0 : return s2

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t

if gcd(a,n) != 1 : 
    m = -1
    
else:
    m = xgcd(a,n)
    while m <= 0:
        m += n
        
print(n-a, m)