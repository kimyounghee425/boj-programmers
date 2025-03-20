dic = {'black': [0,1], 'brown': [1,10], 'red': [2,100], 'orange': [3,1000], 'yellow': [4,10000],
     'green': [5,100000], 'blue': [6,1000000], 'violet': [7,10000000], 'grey': [8,100000000],
     'white': [9,1000000000]}
li = []

for i in range(3):
    li.append(input())
print(int(str(dic[li[0]][0]) + str(dic[li[1]][0])) * dic[li[2]][1])