from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
answer = [0] * n

for i in range(n):
    if arr[i] == i+1:
        continue

    idx = arr.index(i+1)
    arr[i], arr[idx] = arr[idx], arr[i]

    diff = abs(idx - i)
    answer[arr[i] - 1] += diff
    answer[arr[idx] - 1] += diff

for i in answer:
    print(i, end= " ")
