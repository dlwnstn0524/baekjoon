import sys

def min(a,b,c) :
    min = 1000
    if min > a :
        min = a
    if min > b :
        min = b
    if min > c:
        min = c
    return min

t = int(sys.stdin.readline())
dp = [[0 for _ in range(1001)]for _ in range(3)]

for i in range(t) :
    house = list(map(int, sys.stdin.readline()))

for i in range(1, t) :
    dp