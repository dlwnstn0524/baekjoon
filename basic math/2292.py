n = int(input())
cnt = 1
start = 1
end = 1

for i in range(1, 100000):
    if n >= start and n <= end :
        print(cnt)
        break
    cnt += 1
    start = end + 1
    end += i*6