import sys 
from itertools import combinations

def main() :
  N, M = map(int, sys.stdin.readline().split())
  graph = []
  for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().split())))

  chiken_store_list = []
  house_list = []

  for x in range(N) :
    for y in range(N) :
      if graph[x][y] == 1 :
        house_list.append([x+1, y+1])
      elif graph[x][y] == 2 :
        chiken_store_list.append([x+1, y+1])

  chiken_store_combination = list(combinations(chiken_store_list, M))
  answer = 1e9
  for chicken_store_lists in chiken_store_combination :
    temp = 0
    for house in house_list :
      temp_length = 1e9
      house_x, house_y = house
      for chicken_store in chicken_store_lists :
        chicken_x, chicken_y = chicken_store
        temp_length = min(temp_length, abs(chicken_x - house_x) + abs(chicken_y - house_y))
      temp += temp_length
    answer = min(answer, temp)
  print(answer)

main()