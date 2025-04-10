import sys


def gcd_func(a, b):
    while b != 0:
        a, b = b, a % b

    return a


input = sys.stdin.readline
N = int(input())

trees = [int(input()) for _ in range(N)]

gaps = []
for i in range(1, N): 
    gaps.append(trees[i] - trees[i - 1])

gaps_set = list(set(gaps))

gcd = gaps_set[0]
for i in range(1, len(gaps_set)): 
    gcd = gcd_func(gcd, gaps_set[i])

answer_tree_cnt = 0
for gap in gaps: 
    answer_tree_cnt += gap // gcd - 1

print(answer_tree_cnt)