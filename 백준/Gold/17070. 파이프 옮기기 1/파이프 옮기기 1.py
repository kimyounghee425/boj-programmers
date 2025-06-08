import sys
input = sys.stdin.readline

def main() :
  N = int(input())
  graph = []
  for _ in range(N) :
    graph.append(list(map(int, input().split())))

  answer = [[[0] * N for _ in range(N)] for _ in range(N)]
  answer[0][0][1] = 1

  for x in range(0, N) :
    for y in range(2, N) :
      # 가로, 세로
      if graph[x][y] == 0 :
        answer[0][x][y] = answer[0][x][y-1] + answer[2][x][y-1]
        answer[1][x][y] = answer[1][x-1][y] + answer[2][x-1][y]
      # 대각선
      if graph[x][y] == 0 and graph[x-1][y] == 0 and graph[x][y-1] == 0 :
        answer[2][x][y] = answer[0][x-1][y-1] + answer[1][x-1][y-1] + answer[2][x-1][y-1]

  print(answer[0][N-1][N-1] + answer[1][N-1][N-1] + answer[2][N-1][N-1])

main()