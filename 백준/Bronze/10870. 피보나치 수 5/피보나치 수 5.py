N = int(input())
 
def fibonacci(a, b, cnt):
    if N == 0:
        return 0
    elif cnt >= N:
        return b
    else:
        return fibonacci(b, a+b, cnt+1)
 
print(fibonacci(0, 1, 1))