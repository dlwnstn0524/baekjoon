import sys
from copy import deepcopy

input = sys.stdin.readline

arr = list(map(int, input().split()))
N = int(input())
arr2 = list(map(int, input().split()))
m = 600
flag = True

for i in range(len(arr)):
    if arr2.count(i+1) < arr[i]:
        flag = False

if(not flag):
    print(-1)

else :
    for i in range(N):
        needs = deepcopy(arr)
        belt = deepcopy(arr2)
        idx = i
        cnt = 0
        while(True):
            if sum(needs) == 0:
                break
            if needs[belt[idx] - 1] != 0:
                needs[belt[idx] -1] -= 1
                belt[idx] = 0
            idx = (idx + 1) % N
            cnt += 1
        m = min(m, cnt)
    print(m)