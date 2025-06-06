import sys

r, c = map(int, input().split())

rList = []
cList = ["" for i in range(c)]

for i in range(r):
    word = input().strip()
    rList.append(word)
    for k, v in enumerate(word):
        cList[k] += v

strTotal = []
for i in rList:
    splitList = i.split("#")
    for j in splitList:
        if len(j) >= 2:
            strTotal.append(j)
for i in cList:
    splitList = i.split("#")
    for j in splitList:
        if len(j) >= 2:
            strTotal.append(j)

strTotal.sort()
print(strTotal[0])