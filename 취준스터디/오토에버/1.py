import sys
from itertools import permutations

N = int(sys.stdin.readline())
V = list(map(int, sys.stdin.readline().split()))

# 모든 경우의 수에 대해 이진수로 표현했을때 1의 개수를 세어 m값을 갱신하는 반복문
m = 0
for i in permutations(V, 2):
  temp_s = str(bin(sum(i)))[2:]
  temp = temp_s.count("1")
  
  if m < temp:
    m = temp

print(m)