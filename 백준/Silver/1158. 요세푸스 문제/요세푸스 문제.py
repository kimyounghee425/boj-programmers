N, K = map(int, input().split())

def josephus(N, K):
    rest = list(range(1, N+1))
    result = list()
    index = 0
    for i in range(N):
        if len(rest) == 1:
            result.append(rest[0])
            return result
        index += (K-1)
        while index >= len(rest):
            index = index - len(rest)
        result.append(rest[index])
        del rest[index]
    return result

result = josephus(N, K)
result = str(result)
print('<' + str(result)[1:-1] + '>')