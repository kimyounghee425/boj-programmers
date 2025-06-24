import sys

A, B = map(int, sys.stdin.readline().split())

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
    
result = gcd(A, B)
print('1' * result)