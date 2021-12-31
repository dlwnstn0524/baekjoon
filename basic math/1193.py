n = int(input())
start = 1
end = 1
for i in range(1, 1000000):
    if n >= start and n <= end :
        if i % 2 == 1 :
            print("%d/%d"%(i-n+start,n-start+1))
            break
        if i % 2 == 0 :
            print("%d/%d"%(n-start+1,i-n+start))
            break
    start = end + 1
    end += i + 1