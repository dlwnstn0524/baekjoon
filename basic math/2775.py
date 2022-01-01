t = int(input())

def mem(k, n):
    sum = 0
    if k == 0 :
        return n
    else :
        for i in range(1, n+1):
            sum += mem(k-1, i)
        return sum

for i in range(t) :
    k = int(input())
    n = int(input())
    print(mem(k,n))