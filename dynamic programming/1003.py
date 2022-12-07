import sys

def function(n) :
    call_0 = [1, 0]
    call_1 = [0, 1]
    for i in range(2, n+1) :
        call_0.append(call_0[i-1] + call_0[i-2])
        call_1.append(call_1[i-1] + call_1[i-2])
    return call_0[n], call_1[n]



t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0 :
        print("1 0")
    elif n == 1 :
        print("0 1")
    else :
        a, b = map(int, function(n))
        print(a,b)