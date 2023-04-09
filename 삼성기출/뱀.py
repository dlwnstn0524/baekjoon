from collections import deque
n = int(input())
k = int(input())

graph = [[0] * (n) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 2

l = int(input())
dic_turn = dict()
q = deque()
q.append([0, 0])