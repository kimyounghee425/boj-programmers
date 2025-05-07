N = int(input())
N_list = list(map(int,input().split()))
N_dict = {}
for i in N_list:
    if i not in N_dict:
        N_dict[i] = 1
    else:
        N_dict[i] += 1

M = int(input())
M_list = list(map(int,input().split()))
result = []
for i in M_list:
    if i not in N_dict:
        result.append(0)
    else:
        result.append(N_dict[i])
print(*result)