s, k = map(int, input().split())

key = s // k

if s % k == 0:
    print(pow(key, k))
        
else:
    result = 1
    while k != 0:
        if s % k != 0:
            result *= key
            s -= key
            k -= 1
        else:
            result = result * pow(s//k, k)
            k = 0
            s = 0
    print(result)