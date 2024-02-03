import sys
from itertools import combinations

input = sys.stdin.readline
def check(arr):
    # 매개변수로 들어온 배열로 만든 부분집합의 합이 sums에 모두 있다면 True
    # 매개변수로 들어온 배열로 만든 부분집합의 합이 sums에 하나라도 없다면 False
    for i in range(1, 1<<n):
        sel = []
        for j in range(n):
            if i & (1<<j) != 0:
                sel.append(arr[j])
        if sel(sel) not in sums:
            return False
    return True

n = int(input())
sums = list(map(int, input().split()))


# 조합의 경우가 너무 많으므로 뒤에 부분을 몇가지 제외하고 조합을 만든다. 점화식에 의해 유도된 숫자
for cand in combinations(sums[:2**(n-2) + 2], n):
    flag = check(cand)
    if flag:
        print(*cand)
        break