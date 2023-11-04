import sys
from itertools import combinations

X = sys.stdin.readline()
Y = sys.stdin.readline()

nx = len(X)
ny = len(Y)
n = min(nx, ny)

idx_x = [m for m in range(nx)]
idx_y = [m for m in range(ny)]

for i in range(n, 0, -1):
  for j in combinations(idx_x, i):
    cand_x = ''
    for m in j:
      cand_x += X[m]
    for k in combinations(idx_y, i):
      cand_y = ''
      diff = 0
      for m in k:
        cand_y += Y[m]
      for l in range(i):
        if cand_x[l] != cand_y[l]:
          diff += 1
      if diff < 2:
        print(i)
        exit(0)