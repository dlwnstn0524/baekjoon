def dist(d):
    start = 0
    end = 0
    cnt = 0

    for i in range(1, 1000000):
        for j in range(2):
            if d >= start and d <= end :
                return cnt
            start = end + 1
            end = i + end 
            cnt += 1
            


t = int(input())
for i in range(t) :
    x, y = map(int, input().split())
    print(dist(y-x))