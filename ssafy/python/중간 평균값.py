T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    answer = round((sum(arr) - max(arr) - min(arr)) / 8)
    print("#{} {}".format(t, answer))